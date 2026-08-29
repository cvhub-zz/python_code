"""
Lesson 07 Challenge Solution: The Monster Battle Encyclopedia (Pokédex)!
"""

creatures_database = {
    "Pikachu": {"type": "Electric", "hp": 60, "attack": 55, "move": "Thunderbolt"},
    "Charizard": {"type": "Fire / Flying", "hp": 120, "attack": 85, "move": "Flamethrower"},
    "Blastoise": {"type": "Water", "hp": 130, "attack": 80, "move": "Hydro Pump"},
}

print("========================================")
print("📱 POKÉDEX / CREATURE ENCYCLOPEDIA")
print("========================================")
print("Available monsters in database:", list(creatures_database.keys()))

# 1. Lookup a creature
lookup_name = input("\nEnter creature name to inspect: ").strip().capitalize()

if lookup_name in creatures_database:
    c = creatures_database[lookup_name]
    print(f"\n✨ --- {lookup_name.upper()} DATA --- ✨")
    print(f"Type:           {c['type']}")
    print(f"Health Points:  {c['hp']} HP")
    print(f"Attack Power:   {c['attack']}")
    print(f"Signature Move: {c['move']}")
else:
    print(f"\n❌ Creature '{lookup_name}' is not yet in your Pokédex!")

# 2. Add a newly discovered creature
print("\n--- 📝 DISCOVER A NEW CREATURE ---")
new_name = input("Enter new creature name: ").strip().capitalize()
new_type = input("Enter type (e.g. Grass, Psychic): ").strip()
new_hp = int(input("Enter HP: "))
new_atk = int(input("Enter Attack power: "))
new_move = input("Enter signature move: ").strip()

creatures_database[new_name] = {
    "type": new_type,
    "hp": new_hp,
    "attack": new_atk,
    "move": new_move
}

print(f"\n🎉 Successfully registered {new_name} in the encyclopedia!")
print("Updated database index:", list(creatures_database.keys()))

