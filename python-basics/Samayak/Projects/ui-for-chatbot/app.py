from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

# simple in-memory chat history
chat_history = []

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html>
<head>
<title>Local Chat</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

</head>

<body class="bg-dark text-light">

<div class="container py-4" style="max-width: 700px;">
    
    <h4 class="text-center mb-3">Local Chat</h4>

    <div id="chat" class="border rounded p-3 mb-3 bg-secondary-subtle text-dark" 
         style="height: 420px; overflow-y: auto;">
    </div>

    <form class="d-flex gap-2" onsubmit="sendMessage(event)">
        <input id="input" class="form-control" placeholder="Ask something..." autocomplete="off"/>
        <button class="btn btn-info fw-bold" type="submit">Send</button>
    </form>

</div>

<script>
async function sendMessage(e) {
    e.preventDefault();

    let input = document.getElementById("input");
    let chat = document.getElementById("chat");

    let userMsg = input.value;

    if (!userMsg.trim()) return;

    // USER MESSAGE
    chat.innerHTML += `
    <div class="d-flex justify-content-end">
        <div class="bg-info text-dark p-2 rounded mb-2" style="max-width: 75%;">
            ${userMsg}
        </div>
    </div>`;

    input.value = ""; // clear input

    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({prompt: userMsg})
    });

    let data = await res.json();

    let formatted = data.response.replace(/\\n/g, "<br>");

    // BOT MESSAGE (fixed)
    chat.innerHTML += `
    <div class="d-flex justify-content-start">
        <div class="bg-warning text-dark p-2 rounded mb-2" style="max-width: 75%;">
            ${formatted}
        </div>
    </div>`;

    chat.scrollTop = chat.scrollHeight;
    input.focus();
}
</script>

</body>
</html>
"""

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history

    data = request.get_json()
    prompt = data["prompt"]

    # add user message
    chat_history.append(f"User: {prompt}")

    # limit memory (keep it fast)
    if len(chat_history) > 10:
        chat_history.pop(0)

    full_prompt = "\n".join(chat_history) + "\nAssistant:"

    res = requests.post(OLLAMA_URL, json={
        "model": "qwen2:1.5b",
        "prompt": full_prompt,
        "stream": False,
        "num_predict": 60,
        "temperature": 0.2
    })

    response = res.json()["response"]

    # add assistant reply
    chat_history.append(f"Assistant: {response}")

    return jsonify({"response": response})


app.run(port=5000)