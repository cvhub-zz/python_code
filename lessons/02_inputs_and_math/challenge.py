"""
Lesson 02 Challenge: Pizza Party Calculator & Wacky Mad Libs!
============================================================
MISSION 1: Pizza Party Calculator
Help the party host figure out how many pizza slices everyone gets
and what is left over.

MISSION 2: Wacky Mad Libs Story
Collect fun words from the user and print out a crazy story using f-strings!
"""

print("========================================")
print("🍕 MISSION 1: PIZZA PARTY CALCULATOR")
print("========================================")

# TODO 1: Ask the user how many total pizza slices they ordered. Convert it to an integer using int().
# Hint: total_slices = int(input("How many slices in total? "))
total_slices = 0

# TODO 2: Ask the user how many people are at the party. Convert it to an int.
people_count = 1

# TODO 3: Calculate how many whole slices each person gets using integer division (//).
slices_each = 0

# TODO 4: Calculate the leftover slices using modulo (%).
leftovers = 0

# TODO 5: Print a summary using an f-string!
# e.g., "At the party, each of the {people_count} guests gets {slices_each} slices, leaving {leftovers} slice(s)!"
print(f"Each person gets {slices_each} slices with {leftovers} left over.")


print("\n========================================")
print("📖 MISSION 2: WACKY MAD LIBS STORY")
print("========================================")

# TODO 6: Ask the user for:
# - An adjective (e.g. "gigantic", "sparkly")
# - A mythical creature (e.g. "dragon", "unicorn")
# - A food (e.g. "marshmallow", "taco")
# - A number (converted to int)

adj = "TODO"
creature = "TODO"
food = "TODO"
number = 1

# TODO 7: Fill in the f-string story below!
story = f"One day, a {adj} {creature} stomped into town demanding {number} giant {food}s!"
print("\nHere is your wacky story:")
print(story)

