from flask import Flask, render_template, request, redirect
from docx import Document
import sqlite3
from datetime import datetime
from docx import Document

import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import numpy as np
import re

app = Flask(__name__)

DB = "attendance.db"


def get_db():
    return sqlite3.connect(DB)


def init_db():

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        total_classes INTEGER DEFAULT 0,
        attended_classes INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS timetable(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        subject TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        status TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- DOCX ----------------

def read_docx(filepath):

    doc = Document(filepath)

    text = ""

    for p in doc.paragraphs:
        text += p.text + "\n"

    return text


# ---------------- OCR IMAGE ----------------

def extract_text_from_image(filepath):

    img = cv2.imread(filepath)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    text = pytesseract.image_to_string(thresh)

    return text


# ---------------- PARSER ----------------

def parse_timetable_text(text):

    subjects = set()

    tokens = re.findall(r"[A-Z]{2,6}", text)

    ignore = {
        "BREAK",
        "LAB",
        "CSE",
        "CG",
        "DS",
        "SPORTS",
        "NPTEL"
    }

    for t in tokens:

        if t not in ignore:
            subjects.add(t)

    timetable = []

    for s in subjects:
        timetable.append(("Monday", s))

    return timetable


# ---------------- DASHBOARD ----------------

@app.route("/")
def dashboard():

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM subjects")
    subjects = cur.fetchall()

    data = []

    for s in subjects:

        total = s[2]
        attended = s[3]

        percent = 0
        if total > 0:
            percent = round((attended / total) * 100, 2)

        bunks = 0
        if total > 0:
            bunks = int((attended / 0.75) - total)

        data.append({
            "name": s[1],
            "total": total,
            "attended": attended,
            "percent": percent,
            "bunks": bunks
        })

    cur.execute("""
    SELECT id,subject,status,date
    FROM attendance_logs
    ORDER BY id DESC
    LIMIT 10
    """)

    logs = cur.fetchall()

    conn.close()

    return render_template("dashboard.html", subjects=data, logs=logs)


# ---------------- MANUAL TIMETABLE ----------------

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        subject = request.form["subject"]
        day = request.form["day"]

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO timetable(day,subject) VALUES(?,?)",
            (day, subject)
        )

        cur.execute("SELECT * FROM subjects WHERE name=?", (subject,))
        exists = cur.fetchone()

        if not exists:
            cur.execute(
                "INSERT INTO subjects(name) VALUES(?)",
                (subject,)
            )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("upload.html")


# ---------------- ATTENDANCE ----------------

@app.route("/mark", methods=["POST"])
def mark():

    subject = request.form.get("subject")
    status = request.form.get("status")

    if status not in ["present", "absent"]:
        return redirect("/")

    today = datetime.now().strftime("%Y-%m-%d")

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO attendance_logs(subject,status,date) VALUES(?,?,?)",
        (subject, status, today)
    )

    cur.execute(
        "UPDATE subjects SET total_classes = total_classes + 1 WHERE name=?",
        (subject,)
    )

    if status == "present":

        cur.execute(
            "UPDATE subjects SET attended_classes = attended_classes + 1 WHERE name=?",
            (subject,)
        )

    conn.commit()
    conn.close()

    return redirect("/")


# ---------------- UNDO ----------------

@app.route("/undo/<int:log_id>")
def undo(log_id):

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT subject,status FROM attendance_logs WHERE id=?",
        (log_id,)
    )

    log = cur.fetchone()

    if log:

        subject, status = log

        cur.execute(
            "UPDATE subjects SET total_classes = total_classes - 1 WHERE name=?",
            (subject,)
        )

        if status == "present":

            cur.execute(
                "UPDATE subjects SET attended_classes = attended_classes - 1 WHERE name=?",
                (subject,)
            )

        cur.execute(
            "DELETE FROM attendance_logs WHERE id=?",
            (log_id,)
        )

    conn.commit()
    conn.close()

    return redirect("/")


# ---------------- TIMETABLE VIEW ----------------

@app.route("/timetable")
def timetable():

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM timetable")
    rows = cur.fetchall()

    conn.close()

    return render_template("timetable.html", rows=rows)


# ---------------- SUBJECT CALENDAR ----------------

@app.route("/subject/<name>")
def subject_calendar(name):

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT date,status,id
    FROM attendance_logs
    WHERE subject=?
    """, (name,))

    rows = cur.fetchall()

    conn.close()

    logs = {r[0]: {"status": r[1], "id": r[2]} for r in rows}

    return render_template(
        "subject.html",
        subject=name,
        logs=logs
    )


# ---------------- FILE UPLOAD ----------------

@app.route("/upload-file", methods=["POST"])
def upload_file():

    file = request.files.get("file")

    if not file or file.filename == "":
        return redirect("/upload")

    path = "temp_upload"
    os.makedirs(path, exist_ok=True)

    filepath = os.path.join(path, file.filename)

    file.save(filepath)

    text = ""

    if filepath.endswith(".pdf"):

        pages = convert_from_path(filepath)

        for p in pages:
            text += pytesseract.image_to_string(p)

    elif filepath.endswith(".docx"):

        text = read_docx(filepath)

    else:

        text = extract_text_from_image(filepath)

    entries = parse_timetable_text(text)

    conn = get_db()
    cur = conn.cursor()

    for day, subject in entries:

        cur.execute(
            "INSERT INTO timetable(day,subject) VALUES(?,?)",
            (day, subject)
        )

        cur.execute("SELECT * FROM subjects WHERE name=?", (subject,))

        if not cur.fetchone():
            cur.execute("INSERT INTO subjects(name) VALUES(?)", (subject,))

    conn.commit()
    conn.close()

    return redirect("/timetable")


# ---------------- START SERVER ----------------

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
    