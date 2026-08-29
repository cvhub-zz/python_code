"""
Lesson 02 Challenge Solution: Pizza Party Calculator & Mad Libs
"""

print("========================================")
print("🍕 MISSION 1: PIZZA PARTY CALCULATOR")
print("========================================")

total_slices = int(input("How many pizza slices in total? "))
people_count = int(input("How many hungry people are at the party? "))

slices_each = total_slices // people_count
leftovers = total_slices % people_count

print(f"\n🍕 Result: Each of the {people_count} friends gets {slices_each} slices.")
print(f"🐶 Leftover slices for the puppy: {leftovers} slice(s)!\n")


print("========================================")
print("📖 MISSION 2: WACKY MAD LIBS STORY")
print("========================================")

adj = input("Enter a silly adjective (e.g. glowing, smelly): ")
creature = input("Enter a creature (e.g. yeti, cyber-hamster): ")
food = input("Enter a food (e.g. pancake, burrito): ")
number = int(input("Enter a lucky number: "))

story = (
    f"Breaking News! A {adj} {creature} just broke into the city bakery!\n"
    f"It consumed {number} {food}s in under 10 seconds before flying away into outer space!"
)

print("\n--- 🌟 YOUR WACKY STORY ---")
print(story)
