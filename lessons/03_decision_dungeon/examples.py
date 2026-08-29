"""
Lesson 03: Decision Dungeon - Code Examples
Run this file to see how Python makes decisions with if, elif, and else!
"""

print("--- 🎢 Example 1: Rollercoaster Height Checker ---")
rider_height = int(input("Enter your height in centimeters (e.g. 135): "))

if rider_height >= 140:
    print("🎢 Woohoo! You are tall enough for the Mega Loop Rollercoaster!")
elif rider_height >= 110:
    print("🚂 You can ride the Junior Racer Coaster with an adult.")
else:
    print("🎠 You get to enjoy the Merry-Go-Round and bumper cars!")


print("\n--- 🛡️ Example 2: Dungeon Door Lock (Using 'and' / 'or') ---")
player_level = int(input("Enter your player level (1-10): "))
has_gold_key = input("Do you have the Gold Key? (yes/no): ").lower() == "yes"
is_master_thief = input("Are you a Master Thief? (yes/no): ").lower() == "yes"

# Can enter if high level AND has key, OR if they are a master thief who can pick locks!
if (player_level >= 5 and has_gold_key) or is_master_thief:
    print("🔓 *CLICK!* The giant iron vault swings open!")
else:
    print("🔒 *CLANK!* The door is locked tight. Come back when you are ready!")

