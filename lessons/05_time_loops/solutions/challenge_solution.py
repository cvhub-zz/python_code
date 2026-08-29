"""
Lesson 05 Challenge Solution: Countdown & Guessing Game
"""

import random

print("========================================")
print("🚀 MISSION 1: COUNTDOWN TIMER")
print("========================================")

for second in range(10, 0, -1):
    print(f"{second}...")
print("🚀 BLASTOFF TO MARS!\n")


print("========================================")
print("🎲 MISSION 2: GUESS THE SECRET NUMBER")
print("========================================")

secret_number = random.randint(1, 20)
print("I'm thinking of a secret number between 1 and 20. Can you guess it?")

guessed_correctly = False
attempts = 0

while not guessed_correctly:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 BINGO! You found the secret number {secret_number} in {attempts} tries!")
        guessed_correctly = True
    elif guess < secret_number:
        print("📈 Too low! Try a bigger number.")
    else:
        print("📉 Too high! Try a smaller number.")

