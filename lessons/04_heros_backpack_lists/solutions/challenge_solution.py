"""
Lesson 04 Challenge Solution: RPG Inventory & Potion Brewer!
"""

print("========================================")
print("🎒 HERO'S BACKPACK INVENTORY CHALLENGE")
print("========================================")

# Starting backpack
hero_backpack = ["Wooden Shield", "Apple", "Wooden Bow", "Arrow Quiver"]
print("Starting Backpack:", hero_backpack)

# 1. First item and length
print(f"First item: {hero_backpack[0]} | Total items: {len(hero_backpack)}")

# 2. Append Magic Wand
hero_backpack.append("Magic Wand")
print("Added Magic Wand:", hero_backpack)

# 3. Eat the Apple (remove)
hero_backpack.remove("Apple")
print("Ate Apple:", hero_backpack)

# 4. Upgrade Wooden Bow (which is at index 1 now that Apple was removed)
bow_index = hero_backpack.index("Wooden Bow")
hero_backpack[bow_index] = "Dragon Bow of Fire"
print("Upgraded Bow:", hero_backpack)

# 5. Check membership with 'in'
if "Magic Wand" in hero_backpack:
    print("🧙 The hero is ready to cast spells!")
else:
    print("You need to find a wand!")

# 6. Final summary
print("\n🎒 FINAL BACKPACK CONTENTS:")
print(hero_backpack)
print("🎉 Ready for the adventure!")

