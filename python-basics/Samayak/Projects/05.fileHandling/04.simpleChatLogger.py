# Save chat messages in a file (like chat history).

def chat():           
    with open("chat_log.txt", "a") as f:
        while True:
            msg = input("You: ")
            if msg.lower() == "exit":
                break
        f.write(f"You: {msg}\n")
    print("Chat saved successfully!")
chat()  