# ❓ Simple Quiz Game
# Author: Piyush (Your Name)

print("🎯 Welcome to the Python Quiz Game!")
print("Answer the questions and see your score.\n")

# Step 1: Create a list of questions
quiz = [
    {
        "question": "1️⃣ What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2️⃣ Which programming language is known as the 'Mother of all languages'?",
        "options": ["A. C", "B. Java", "C. Python", "D. Assembly"],
        "answer": "A"
    },
    {
        "question": "3️⃣ What is the shortcut key to copy in Windows?",
        "options": ["A. Ctrl + X", "B. Ctrl + C", "C. Ctrl + V", "D. Ctrl + Z"],
        "answer": "B"
    },
    {
        "question": "4️⃣ What does HTML stand for?",
        "options": [
            "A. Hyperlinks and Text Markup Language",
            "B. Home Tool Markup Language",
            "C. Hyper Text Markup Language",
            "D. Hyper Transfer Main Language"
        ],
        "answer": "C"
    }
]

# Step 2: Initialize score
score = 0

# Step 3: Loop through each question
for q in quiz:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    user_ans = input("Your answer (A/B/C/D): ").upper()

    # Step 4: Check answer
    if user_ans == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

# Step 5: Final Score
print("🎓 Quiz Over!")
print(f"Your final score is {score}/{len(quiz)}")

# Step 6: Performance message
if score == len(quiz):
    print("🏆 Excellent! You got all correct!")
elif score >= len(quiz)//2:
    print("😊 Good job! Keep practicing.")
else:
    print("😅 You need more practice.")
