"""
Lesson 07 Challenge: The Monster Battle Encyclopedia (Pokédex)!
===============================================================
MISSION:
Build an interactive Monster Encyclopedia where the player can:
1. View a monster's stats by looking up its name.
2. Add a brand new discovered monster to the database!

Follow the TODO instructions below.
"""

# Database of magical creatures
creatures_database = {
    "Pikachu": {"type": "Electric", "hp": 60, "attack": 55, "move": "Thunderbolt"},
    "Charizard": {"type": "Fire / Flying", "hp": 120, "attack": 85, "move": "Flamethrower"},
    "Blastoise": {"type": "Water", "hp": 130, "attack": 80, "move": "Hydro Pump"},
}

print("========================================")
print("📱 POKÉDEX / CREATURE ENCYCLOPEDIA")
print("========================================")
print("Available monsters in database:", list(creatures_database.keys()))

# TODO 1: Ask the user to enter a monster name to look up
# lookup_name = input("\nEnter creature name to inspect: ").strip()


# TODO 2: Check if lookup_name is in creatures_database using 'in'
# IF found:
#   Print their Type, HP, Attack, and Signature Move!
# ELSE:
#   Print "Creature not found in database!"


# TODO 3: Add a new creature!
# Ask the user for:
# - New creature name
# - Element type
# - HP (int)
# - Attack (int)
# - Move name
# And save it into creatures_database[new_name] = {...}


# TODO 4: Print the updated list of creature names in the encyclopedia!

