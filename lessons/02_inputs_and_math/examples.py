"""
Lesson 02: Inputs and Math - Code Examples
Run this file to see interactive inputs and math calculations!
"""

print("--- 🧙‍♂️ Step 1: Interactive Wizard Greeting ---")
wizard_name = input("Enter your wizard name: ")
favorite_element = input("What is your magic element (Fire, Ice, Lightning)? ")

# Using f-strings to combine variables into sentences
print(f"\n⚡ Welcome, Wizard {wizard_name}! You wield the power of {favorite_element}!\n")

print("--- 🧮 Step 2: Level & XP Calculator ---")
current_level = int(input("Enter your current level (e.g. 3): "))
xp_per_level = 100

total_xp = current_level * xp_per_level
next_level_xp = (current_level + 1) * xp_per_level

print(f"Total XP earned so far: {total_xp}")
print(f"XP needed for Level {current_level + 1}: {next_level_xp}")

print("\n--- 🍕 Step 3: Pizza Slicing Math ---")
total_slices = 17
eaters = 4

slices_per_person = total_slices // eaters    # Whole slices
leftover_slices = total_slices % eaters       # Leftover slices (remainder)

print(f"We have {total_slices} slices for {eaters} people.")
print(f"Each person eats: {slices_per_person} slices.")
print(f"Leftover slices: {leftover_slices} slice(s).")

