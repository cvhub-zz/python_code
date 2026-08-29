"""
Lesson 05 Challenge: Rocket Blastoff & The Secret Number Guessing Game!
=====================================================================
MISSION 1: Rocket Countdown
Use a for loop and range() to count from 10 down to 1, then print BLASTOFF!

MISSION 2: The Secret Number Guessing Game
The computer picks a secret number from 1 to 20.
The player has to guess it, and the computer tells them if their guess
is "Too High" or "Too Low" until they get it right!
"""

import random

print("========================================")
print("🚀 MISSION 1: COUNTDOWN TIMER")
print("========================================")

# TODO 1: Write a for loop with range(10, 0, -1) to count down from 10 to 1!
# Inside the loop, print the number.
# After the loop, print "🚀 BLASTOFF TO MARS!"



print("\n========================================")
print("🎲 MISSION 2: GUESS THE SECRET NUMBER")
print("========================================")

secret_number = random.randint(1, 20)
print("I'm thinking of a secret number between 1 and 20. Can you guess it?")

guessed_correctly = False
attempts = 0

# TODO 2: Write a while loop that runs while guessed_correctly is False
# Inside the loop:
# 1. Ask the player for a guess: guess = int(input("Enter your guess: "))
# 2. Increase attempts by 1
# 3. IF guess == secret_number:
#      print victory message with attempts count!
#      set guessed_correctly = True
#    ELIF guess < secret_number:
#      print "📈 Too low! Try a bigger number."
#    ELSE:
#      print "📉 Too high! Try a smaller number."

while not guessed_correctly:
    # Write your guessing game code here!
    break # Remove this break after writing your loop!
