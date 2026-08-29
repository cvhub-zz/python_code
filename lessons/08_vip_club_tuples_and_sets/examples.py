"""
Lesson 08: Tuples & Sets - Code Examples
Run this file to see how tuples lock data and sets eliminate duplicates!
"""

# -------------------------------------------------------------
# 1. TUPLES (Immutable coordinates & RGB colors)
# -------------------------------------------------------------
print("--- 📍 Example 1: Game Map Coordinates (Tuples) ---")
castle_location = (150, 300)
print("Castle Map Pin:", castle_location)

# Unpacking coordinate tuple
castle_x, castle_y = castle_location
print(f"Castle is at X-coordinate: {castle_x}, Y-coordinate: {castle_y}")

# Game Color Palette (RGB)
LASER_GREEN = (50, 255, 50)
print(f"Laser color tuple: {LASER_GREEN}")


# -------------------------------------------------------------
# 2. SETS (Unique Badges & Deduplication)
# -------------------------------------------------------------
print("\n--- 🎖️ Example 2: Unlocked Achievement Badges (Sets) ---")

# Let's say a player triggers the "First Kill" badge multiple times
raw_badge_events = ["First Kill", "Treasure Hunter", "First Kill", "Level 10", "Treasure Hunter"]

# Converting list to set automatically removes all duplicate awards!
unlocked_badges = set(raw_badge_events)
print("Unique badges earned:", unlocked_badges)

# Adding a new badge with .add()
unlocked_badges.add("Dragon Slayer")
print("After defeating boss:", unlocked_badges)


# -------------------------------------------------------------
# 3. SET OPERATIONS (Union, Intersection, Difference)
# -------------------------------------------------------------
print("\n--- ⚔️ Example 3: Finding Shared Skills & Counter Attacks ---")

my_team_elements = {"Fire", "Lightning", "Earth"}
dungeon_elements = {"Water", "Lightning", "Ice"}

# Intersection (&): Elements present in BOTH sets
shared = my_team_elements & dungeon_elements
print("⚡ Shared Elements (Overlap):", shared)

# Union (|): All elements combined
all_elements = my_team_elements | dungeon_elements
print("🌈 All elements combined:", all_elements)

# Difference (-): Team elements not in dungeon
unique_to_team = my_team_elements - dungeon_elements
print("🔥 Team elements not in dungeon:", unique_to_team)
