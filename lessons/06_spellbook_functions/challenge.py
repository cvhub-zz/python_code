"""
Lesson 06 Challenge: Magic Battle Spellbox!
===========================================
MISSION:
Create reusable function spells for a fantasy battle arena!

Follow the TODO instructions below.
"""

# TODO 1: Create a function named show_character_card(name, role, hp)
# It should print out:
# "=== [name] the [role] (HP: [hp]) ==="
def show_character_card(name, role, hp):
    pass  # Replace 'pass' with your code!


# TODO 2: Create a function named attack(attacker_name, defender_name, weapon_damage, is_critical=False)
# If is_critical is True, damage is doubled (weapon_damage * 2).
# It should print:
# "[attacker_name] strikes [defender_name] for [damage] damage!"
# And it should RETURN the damage dealt!
def attack(attacker_name, defender_name, weapon_damage, is_critical=False):
    # Calculate damage and return it
    return 0


# =============================================================
# TEST YOUR SPELLBOOK!
# =============================================================
print("--- ⚔️ BATTLE START ---")
hero_hp = 100
goblin_hp = 50

# Test character card display
show_character_card("Sir Galahad", "Paladin", hero_hp)
show_character_card("Grumble", "Goblin King", goblin_hp)

# Test attack spell
dmg = attack("Sir Galahad", "Grumble", 25, is_critical=True)
goblin_hp -= dmg
print(f"Grumble the Goblin has {goblin_hp} HP remaining!")

