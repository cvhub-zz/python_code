"""
🎮 CAPSTONE GAME: The Dragon's Shadow RPG
=========================================
A complete Python text adventure game combining:
- Variables & Data Types
- Math & f-Strings
- If / Elif / Else Conditionals
- Lists (Hero Inventory)
- For & While Loops
- Functions (Modular game actions)
- Dictionaries (Player & Monster Stats)
- Tuples (Coordinates) & Sets (Badges)

Run this file and embark on your quest!
"""

import random
import time

# --- DATA STRUCTURES ---

# Hero Profile (Dictionary)
player = {
    "name": "Hero",
    "hp": 100,
    "max_hp": 100,
    "attack": 20,
    "gold": 30,
    "level": 1
}

# Hero Inventory (List)
inventory = ["Wooden Sword", "Health Potion"]

# Unlocked Badges (Set for unique badges)
badges = set()

# Current Map Coordinates (Tuple)
current_location = (0, 0)


# --- FUNCTIONS (GAME ACTIONS) ---

def show_status():
    """Prints the player's current health, gold, items, and badges."""
    print("\n" + "=" * 45)
    print(f"🧙 HERO: {player['name']} (Lvl {player['level']})")
    print(f"❤️  HP: {player['hp']}/{player['max_hp']}  |  🪙 GOLD: {player['gold']}")
    print(f"🎒 BACKPACK: {', '.join(inventory) if inventory else 'Empty'}")
    print(f"🎖️  BADGES: {', '.join(badges) if badges else 'None yet'}")
    print(f"📍 MAP PIN: {current_location}")
    print("=" * 45)


def heal_player():
    """Uses a potion from inventory to restore HP."""
    if "Health Potion" in inventory:
        inventory.remove("Health Potion")
        heal_amount = 35
        player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
        print(f"\n🧪 Slurp! Restored {heal_amount} HP. Current HP: {player['hp']}/{player['max_hp']}")
    else:
        print("\n❌ You don't have any Health Potions in your backpack!")


def visit_shop():
    """Shop menu to spend gold on gear and potions."""
    print("\n🏪 --- YE OLDE ITEM SHOP ---")
    print("1. Health Potion (15 Gold) - Restores 35 HP")
    print("2. Steel Sword (40 Gold)    - Increases Attack to 35")
    print("3. Dragon Shield (50 Gold)  - Increases Max HP to 140")
    print("4. Exit Shop")

    choice = input("\nWhat would you like to buy? (1-4): ").strip()
    if choice == "1":
        if player["gold"] >= 15:
            player["gold"] -= 15
            inventory.append("Health Potion")
            print("🛍️ Purchased a Health Potion!")
        else:
            print("💸 Not enough gold!")
    elif choice == "2":
        if player["gold"] >= 40:
            player["gold"] -= 40
            player["attack"] = 35
            inventory.append("Steel Sword")
            print("⚔️ Purchased Steel Sword! Attack increased to 35!")
        else:
            print("💸 Not enough gold!")
    elif choice == "3":
        if player["gold"] >= 50:
            player["gold"] -= 50
            player["max_hp"] = 140
            player["hp"] = 140
            inventory.append("Dragon Shield")
            print("🛡️ Purchased Dragon Shield! Max HP increased to 140!")
        else:
            print("💸 Not enough gold!")
    elif choice == "4":
        print("👋 Come back soon!")
    else:
        print("❓ Invalid shop selection.")


def battle_monster(monster_name, monster_hp, monster_atk, gold_reward, badge_name=None):
    """Handles turn-based battle loop with a monster."""
    print(f"\n⚔️ A wild {monster_name} (HP: {monster_hp}) jumps out from the shadows!")

    while monster_hp > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | {monster_name} HP: {monster_hp}")
        action = input("Action: (1) Attack  (2) Drink Potion  (3) Run: ").strip()

        if action == "1":
            # Hero attacks
            crit = random.choice([False, False, True])  # 33% chance of critical hit
            dmg = player["attack"] * 2 if crit else player["attack"]
            crit_text = " [💥 CRITICAL HIT!]" if crit else ""
            monster_hp -= dmg
            print(f"🗡️ You hit {monster_name} for {dmg} damage!{crit_text}")

            if monster_hp <= 0:
                print(f"🎉 Victory! You defeated the {monster_name}!")
                player["gold"] += gold_reward
                print(f"🪙 Found {gold_reward} Gold!")
                if badge_name:
                    badges.add(badge_name)
                    print(f"🎖️ NEW BADGE UNLOCKED: [{badge_name}]!")
                return True

            # Monster attacks back
            monster_dmg = random.randint(monster_atk - 5, monster_atk + 5)
            player["hp"] -= monster_dmg
            print(f"💥 {monster_name} hits you for {monster_dmg} damage!")

            if player["hp"] <= 0:
                print("\n💀 You were defeated in battle... Game Over!")
                return False

        elif action == "2":
            heal_player()
        elif action == "3":
            print(f"🏃💨 You ran away safely from {monster_name}!")
            return False
        else:
            print("❓ Invalid choice! The monster glares at you.")

    return player["hp"] > 0


# --- MAIN GAME LOOP ---

def main():
    print("==============================================")
    print("🐉  WELCOME TO THE DRAGON'S SHADOW RPG  🐉")
    print("==============================================")

    hero_name = input("Enter your hero's name: ").strip()
    if hero_name:
        player["name"] = hero_name

    badges.add("Novice Adventurer")
    print(f"\nWelcome, {player['name']}! Your quest begins.")

    game_running = True
    while game_running and player["hp"] > 0:
        show_status()
        print("\nWhere do you want to explore?")
        print("1. 🌲 Whispering Woods (Fight Goblins / Slimes)")
        print("2. 🏔️ Rocky Mountains (Fight Mountain Troll)")
        print("3. 🌋 The Dragon's Lair (Boss Battle!)")
        print("4. 🏪 Ye Olde Item Shop")
        print("5. 🧪 Drink Health Potion")
        print("6. 🚪 Quit Quest")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            # Random encounter
            monster = random.choice([
                {"name": "Green Slime", "hp": 25, "atk": 8, "gold": 12, "badge": "Slime Squisher"},
                {"name": "Forest Goblin", "hp": 40, "atk": 14, "gold": 20, "badge": "Goblin Hunter"}
            ])
            battle_monster(monster["name"], monster["hp"], monster["atk"], monster["gold"], monster["badge"])

        elif choice == "2":
            battle_monster("Mountain Troll", 80, 22, 50, "Troll Buster")

        elif choice == "3":
            print("\n🔥 You enter the scorching magma caverns...")
            if "Dragon Shield" not in inventory and player["attack"] < 30:
                print("⚠️ WARNING: You feel under-equipped for the mighty Dragon!")
            proceed = input("Do you dare challenge the Dragon? (yes/no): ").lower().strip()
            if proceed == "yes":
                won = battle_monster("Ancient Red Dragon", 160, 32, 200, "Dragon Slayer")
                if won:
                    print("\n" + "🌟" * 20)
                    print("🏆 CONGRATULATIONS! You defeated the Ancient Red Dragon and saved the Realm!")
                    print("🌟" * 20)
                    game_running = False

        elif choice == "4":
            visit_shop()
        elif choice == "5":
            heal_player()
        elif choice == "6":
            print(f"\nThanks for playing, {player['name']}! See you next time!")
            game_running = False
        else:
            print("❓ Unknown command. Try typing 1, 2, 3, 4, 5, or 6.")

    if player["hp"] <= 0:
        print("\n💀 Your journey has ended. Rerun the game to try again!")


if __name__ == "__main__":
    main()

