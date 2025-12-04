import time

# ---------------------------
# GAME DATA (WITH CLUES)
# ---------------------------

PUZZLES = [
    {
        "question": "Clue 1: You find a torn diary. It says: 'I have keys but no locks.' What is it?",
        "answer": "keyboard",
        "hint": "You use it with a computer to type."
    },
    {
        "question": "Clue 2: A note on the wall says: 'Half of 8 will open the safe.' Enter the number:",
        "answer": "4",
        "hint": "Divide 8 by 2."
    },
    {
        "question": "Clue 3: A code is written in blood: '2 + 3 × 2'. Enter the correct answer:",
        "answer": "8",
        "hint": "Follow BODMAS rule."
    }
]

MURDERER = "butler"

TOTAL_TIME = 60  # 60 seconds for demo (you can change to 3600 for 1 hour)
TIME_PENALTY = 5  # seconds reduced for each hint

# ---------------------------
# GAME START
# ---------------------------

print("\n🕵️ MURDER AT MIDNIGHT - ESCAPE ROOM GAME 🕛")
print("You are trapped inside a dark mansion.")
print("Solve all the clues and find the real murderer before time runs out!")
print("Type 'hint' anytime to get a clue (time will be reduced).")

start_time = time.time()
mistakes = 0
hints_used = 0

# ---------------------------
# PUZZLE LOOP
# ---------------------------

for i, puzzle in enumerate(PUZZLES):
    print("\n-----------------------------------")
    print(f"Puzzle {i + 1}")
    print(puzzle["question"])

    while True:
        elapsed = int(time.time() - start_time)
        remaining = TOTAL_TIME - elapsed

        if remaining <= 0:
            print("\n⏰ TIME OVER! The killer caught you!")
            print("GAME OVER ❌")
            exit()

        print("Time Left:", remaining, "seconds")
        user_input = input("Enter your answer (or type 'hint'): ").lower().strip()

        if user_input == "hint":
            print("HINT:", puzzle["hint"])
            start_time += TIME_PENALTY
            hints_used += 1
            continue

        if user_input == puzzle["answer"]:
            print("✅ Correct! Next clue unlocked.")
            break
        else:
            print("❌ Wrong answer! Try again.")
            mistakes += 1

# ---------------------------
# FINAL MURDERER QUESTION
# ---------------------------

print("\n-----------------------------------")
print("FINAL CLUE: The murderer loves KEYS and MUSIC.")
print("Who is the murderer?")
print("Options: Butler / Chef / Gardener")

final_answer = input("Enter the murderer: ").lower().strip()

elapsed = int(time.time() - start_time)
remaining = TOTAL_TIME - elapsed

if remaining <= 0:
    print("\n⏰ TIME OVER! The killer escaped!")
    print("GAME OVER ❌")
elif final_answer == MURDERER:
    print("\n🎉 YOU ESCAPED SUCCESSFULLY!")
    print("✅ You found the real murderer:", MURDERER.upper())
else:
    print("\n❌ WRONG CHOICE!")
    print("The real murderer was:", MURDERER.upper())
    print("GAME OVER!")

# ---------------------------
# SCORE SUMMARY
# ---------------------------

print("\n📊 GAME SUMMARY")
print("Time Left:", remaining if remaining > 0 else 0)
print("Mistakes Made:", mistakes)
print("Hints Used:", hints_used)
print("\nTHANK YOU FOR PLAYING! 🕵️")
