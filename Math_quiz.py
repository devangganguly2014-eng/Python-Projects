import random

print("🎯 Welcome to Math Quiz Game! 🧮")
print("Let's see how many math questions you can answer correctly./n ") 

score = 0
for i in range(5):  # You’ll get 5 random questions
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])
    
    # Correct answer
    if operator == "+":
        correct = num1 + num2
    elif operator == "-":
        correct = num1 - num2
    else:
        correct = num1 * num2

    # Ask the question
    print(f"Question {i+1}: What is {num1} {operator} {num2}?")
    answer = int(input("👉 Your answer: "))

    if answer == correct:
        print("✅ Correct! Great job!\n")
        score += 1
    else:
        print(f"❌ Oops! The right answer was {correct}\n")

print(f"🏁 Quiz Over! Your final score is: {score}/5 🎉")

if score == 5:
    print("🌟 Outstanding, Devang! You’re a math genius!")
elif score >= 3:
    print("👍 Nice work! You’re getting really good at this!")
else:
    print("😅 Keep practicing, champ — you’ll nail it next time!")
