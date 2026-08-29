"""
Lesson 07: Monster Vault (Dictionaries) - Code Examples
Run this file to see how dictionaries store and organize key-value pairs!
"""

# 1. Creating a character dictionary
hero = {
    "name": "Aria Skywhisper",
    "element": "Wind",
    "hp": 120,
    "attack": 35,
    "speed": 80
}

print("--- 🧙 Character Sheet ---")
print(f"Hero Name: {hero['name']}")
print(f"Element:   {hero['element']}")
print(f"HP:        {hero['hp']}")


# 2. Modifying & Adding new keys
print("\n--- ⚡ Equipping Boots of Swiftness (+20 Speed) & Ring of Power ---")
hero["speed"] += 20
hero["ring"] = "Ring of Invisibility"  # Adding new key

print(f"Updated Speed: {hero['speed']}")
print(f"Equipped Ring: {hero['ring']}")


# 3. Safe lookup with .get()
print("\n--- 🛡️ Checking for rare artifacts ---")
pet = hero.get("pet", "No companion pet yet")
print(f"Pet Status: {pet}")


# 4. Nested Dictionary: A Mini Monster Bestiary / Pokedex
bestiary = {
    "Goblin": {"hp": 30, "attack": 10, "loot": "Copper Dagger"},
    "Frost Wolf": {"hp": 65, "attack": 25, "loot": "Ice Fur"},
    "Red Dragon": {"hp": 300, "attack": 75, "loot": "Dragon Scale Armor"}
}

print("\n--- 🐉 Monster Bestiary Lookup ---")
target_monster = "Frost Wolf"
if target_monster in bestiary:
    info = bestiary[target_monster]
    print(f"Name:   {target_monster}")
    print(f"HP:     {info['hp']}")
    print(f"Attack: {info['attack']}")
    print(f"Drops:  {info['loot']}")
