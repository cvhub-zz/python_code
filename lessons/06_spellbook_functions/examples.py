"""
Lesson 06: Spellbook Functions - Code Examples
Run this file to see how functions organize and reuse code!
"""

# 1. Simple Function without parameters
def draw_banner():
    print("*" * 40)
    print("✨ --- WIZARD BATTLE ARENA --- ✨")
    print("*" * 40)

draw_banner()


# 2. Function with parameters
def cast_spell(spell_name, target):
    print(f"✨ Casting [{spell_name}] directly at {target}!")

cast_spell("Frost Ray", "Ice Golem")
cast_spell("Thunderbolt", "Dark Sorcerer")


# 3. Function with a return value
def heal_player(current_health, potion_power, max_health=100):
    new_health = current_health + potion_power
    if new_health > max_health:
        new_health = max_health  # Cannot exceed max health!
    return new_health

player_hp = 65
print(f"\nPlayer currently has {player_hp} HP.")

# Drinking a +20 potion
player_hp = heal_player(player_hp, 20)
print(f"After drinking Regular Potion: {player_hp} HP")

# Drinking a +50 Super Potion (capped at 100 max)
player_hp = heal_player(player_hp, 50)
print(f"After drinking Super Potion: {player_hp} HP (Max reached!)")

