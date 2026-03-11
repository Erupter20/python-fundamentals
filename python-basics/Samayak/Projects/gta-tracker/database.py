import sqlite3

DB_NAME = "gta.db"


def connect():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player TEXT,
        name TEXT,
        category TEXT,
        subcategory TEXT,
        price INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS upgrades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player TEXT,
        property_name TEXT,
        upgrade TEXT,
        price INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS finance (
        player TEXT PRIMARY KEY,
        cash INTEGER
    )
    """)

    conn.commit()
    conn.close()


# ---------------------
# ASSETS
# ---------------------

def add_asset(player, name, category, subcategory, price):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO assets VALUES(NULL,?,?,?,?,?)",
        (player, name, category, subcategory, price)
    )

    conn.commit()
    conn.close()


def get_assets(player):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT name, category, subcategory, price FROM assets WHERE player=?",
        (player,)
    )

    rows = cur.fetchall()

    conn.close()

    return rows


def total_assets(player):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT SUM(price) FROM assets WHERE player=?",
        (player,)
    )

    total = cur.fetchone()[0]

    conn.close()

    return total if total else 0


# ---------------------
# UPGRADES
# ---------------------

def add_upgrade(player, property_name, upgrade, price):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO upgrades VALUES(NULL,?,?,?,?)",
        (player, property_name, upgrade, price)
    )

    conn.commit()
    conn.close()


def get_upgrades(player):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT property_name, upgrade, price FROM upgrades WHERE player=?",
        (player,)
    )

    rows = cur.fetchall()

    conn.close()

    return rows


def total_upgrades(player):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT SUM(price) FROM upgrades WHERE player=?",
        (player,)
    )

    total = cur.fetchone()[0]

    conn.close()

    return total if total else 0


# ---------------------
# CASH
# ---------------------

def get_cash(player):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT cash FROM finance WHERE player=?",
        (player,)
    )

    row = cur.fetchone()

    conn.close()

    if row:
        return row[0]

    return 0


def update_cash(player, cash):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO finance(player,cash)
    VALUES(?,?)
    ON CONFLICT(player)
    DO UPDATE SET cash=excluded.cash
    """, (player, cash))

    conn.commit()
    conn.close()