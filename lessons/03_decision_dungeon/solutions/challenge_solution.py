"""
Lesson 03 Challenge Solution: The Haunted Castle Escape!
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

if choice == "up":
    print("\n👻 You climb the creaky stairs and meet Casper the friendly ghost!")
    print("Casper smiles and says: 'Take this magic shield, brave adventurer!'")
    print("🏆 VICTORY: You gained a magical artifact and safely explored the tower!")

elif choice == "down":
    print("\n🦇 You descend into the damp, shadowy basement...")
    flashlight = input("Do you turn on your flashlight? (yes/no): ").lower().strip()
    
    if flashlight == "yes":
        print("💡 The light beams across the room! You spot an unlocked chest filled with gold coins! 💰")
        print("🏆 VICTORY: You escaped with a fortune!")
    else:
        print("🌑 *THUD!* In the pitch black, you tripped over a sleeping goblin!")
        print("The goblin wakes up, gets mad, and chases you back outside! 🏃💨")

elif choice == "outside":
    print("\n🌸 You push open the iron doors leading to the moonlit garden.")
    print("You follow a stone path through fragrant roses and find a secret exit gate!")
    print("🎉 VICTORY: You successfully escaped the haunted castle!")

else:
    print("\n❓ You were too confused by the options and stood still as the clock struck midnight! ⏰")
