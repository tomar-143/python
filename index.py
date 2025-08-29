import time
import random
import json

# ====== QUIZ DATA ======
normal_questions = {
    "What is the capital of France?": "Paris",
    "2 + 5 = ?": "7",
    "Python was created by?": "Guido van Rossum",
    "What is the chemical symbol for gold?": "Au",
    "In which year did India gain independence?": "1947",
    "What is the smallest composite number?": "4"
}

mcq_questions = [
    {
        "question": "Capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Jaipur"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["A) HTML", "B) Python", "C) C++", "D) CSS"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean?",
        "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
        "answer": "C"
    },
    {
        "question":"In Python, which keyword is used to define a function?",
        "options": ["A) define","B) func", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question":"Which of the following is not an OOP concept?",
        "options": ["A) Encapsulation","B) Polymorphism", "C) Inheritance", "D) Compilation"],
        "answer": "D"
    },
    {
        "question":"Which method is used in Python to add an element to a list?",
        "options": ["A) append()","B) add()", "C) push()", "D) insert()"],
        "answer": "A"
    }

]

SCORE_FILE = "quiz_scores.json"

# ====== SAVE SCORE FUNCTION ======
def save_score(username, mode, score, total):
    score_data = {
        "username": username,
        "mode": mode,
        "score": score,
        "total": total,
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        with open(SCORE_FILE, "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []
    
    scores.append(score_data)
    
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)
    
    print("\n💾 Score saved successfully!")

# ====== NORMAL QUIZ ======
def normal_quiz():
    questions = list(normal_questions.items())
    random.shuffle(questions)
    score = 0
    
    for q, a in questions:
        ans = input(f"{q} ").strip()
        if ans.lower() == a.lower():
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! Correct answer: {a}")
    return score, len(questions)

# ====== MCQ QUIZ ======
def mcq_quiz():
    questions = mcq_questions[:]
    random.shuffle(questions)
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"]:
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    return score, len(questions)

# ====== TIMED QUIZ ======
def timed_quiz():
    questions = list(normal_questions.items())
    random.shuffle(questions)
    score = 0
    time_limit = 10  # seconds per question
    
    for q, a in questions:
        print("\n" + q)
        start = time.time()
        ans = input(f"Answer (you have {time_limit}s): ").strip()
        elapsed = time.time() - start
        
        if elapsed > time_limit:
            print("⏳ Time's up!")
        elif ans.lower() == a.lower():
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! Correct: {a}")
    return score, len(questions)

# ====== MAIN PROGRAM ======
def main():
    print("=== Ultimate Quiz Application ===")
    username = input("Enter your name: ").strip()
    
    print("\nChoose a mode:")
    print("1) Normal Quiz")
    print("2) MCQ Quiz")
    print("3) Timed Quiz")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        score, total = normal_quiz()
        mode = "Normal"
    elif choice == "2":
        score, total = mcq_quiz()
        mode = "MCQ"
    elif choice == "3":
        score, total = timed_quiz()
        mode = "Timed"
    else:
        print("Invalid choice!")
        return
    
    print(f"\n🏆 {username}, your score: {score}/{total}")
    save_score(username, mode, score, total)

# ====== RUN ======
if __name__ == "__main__":
    main()
