"""
Lesson 06 Challenge Solution: Magic Battle Spellbox!
"""

def show_character_card(name, role, hp):
    print(f"=== 🛡️ {name} the {role} (HP: {hp}) ===")

def attack(attacker_name, defender_name, weapon_damage, is_critical=False):
    actual_damage = weapon_damage * 2 if is_critical else weapon_damage
    crit_tag = " [💥 CRITICAL HIT!]" if is_critical else ""
    print(f"{attacker_name} strikes {defender_name} for {actual_damage} damage!{crit_tag}")
    return actual_damage

# Test the Battle
print("--- ⚔️ BATTLE START ---")
hero_hp = 100
goblin_hp = 50

show_character_card("Sir Galahad", "Paladin", hero_hp)
show_character_card("Grumble", "Goblin King", goblin_hp)

print("\n--- ROUND 1 ---")
dmg = attack("Sir Galahad", "Grumble", 25, is_critical=True)
goblin_hp -= dmg

if goblin_hp <= 0:
    print(f"\n🏆 Grumble the Goblin King was defeated! Sir Galahad is victorious!")
else:
    print(f"Grumble has {goblin_hp} HP left!")
