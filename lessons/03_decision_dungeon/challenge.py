"""
Lesson 03 Challenge: The Haunted Castle Escape!
==============================================
MISSION:
Build a "Choose Your Own Adventure" mini-game where the player
explores a spooky haunted castle and makes choices.

Use if, elif, and else to create different story endings!
"""

print("========================================")
print("🏰 WELCOME TO THE HAUNTED CASTLE ESCAPE")
print("========================================")
print("You wake up in the entrance hall of an ancient castle.")
print("Before you are three paths:")
print("1. The Creaky Staircase (up)")
print("2. The Dark Basement (down)")
print("3. The Mysterious Garden (outside)")

choice = input("\nWhich path do you take? (up/down/outside): ").lower().strip()

# TODO 1: Check if choice is "up"
# - Print that they encounter a friendly ghost who gives them a magic floating shield.
if choice == "up":
    print("👻 You climb the creaky stairs and meet Casper the friendly ghost!")
    print("He hands you a glowing silver shield!")

# TODO 2: Check with elif if choice is "down"
# - Ask the player if they want to turn on their flashlight (yes/no).
# - Use a nested 'if' to check their answer!
elif choice == "down":
    print("🦇 You walk down into the chilly darkness...")
    # TODO 2b: Ask: flashlight = input("Do you turn on your flashlight? (yes/no): ")
    # If yes -> You spot a treasure chest!
    # Else -> You trip over a sleepy goblin!

# TODO 3: Check with elif if choice is "outside"
# - Print that they found a hidden exit and escaped into the sunshine!

# TODO 4: Use else for any invalid input
# - Print: "You wandered around in circles and got lost in the fog!"
else:
    print("❓ You wandered around in circles and got lost in the fog!")
