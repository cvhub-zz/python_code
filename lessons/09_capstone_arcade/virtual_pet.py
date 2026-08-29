"""
🎮 CAPSTONE GAME: CyberPet Tamagotchi Simulator
===============================================
A virtual pet simulator combining:
- Dictionaries (Pet stats & moods)
- Lists & Sets (Learned tricks & foods)
- Loops (Live simulation loop)
- Functions (Care actions: feed, play, sleep, trick)
- Conditional logic (Mood changes based on stats)
"""

import random

# --- PET DATA ---
pet = {
    "name": "Sparky",
    "species": "Dragon Puppy",
    "hunger": 50,      # 0 = Full, 100 = Starving
    "happiness": 70,   # 0 = Sad, 100 = Ecstatic
    "energy": 80,      # 0 = Exhausted, 100 = Hyper
    "cleanliness": 90  # 0 = Filthy, 100 = Sparkling
}

learned_tricks = ["Sit", "Wag Tail"]
unlocked_achievements = {"Pet Parent"}


# --- ASCII ART HELPERS ---

def draw_pet(mood):
    """Draws different ASCII art depending on pet mood."""
    if mood == "ecstatic":
        print(r"""
          / \__
         (    @\___   ✨ *Barks happily!*
         /         O  
        /   (_____/   
       /_____/   U
        """)
    elif mood == "sleepy":
        print(r"""
          / \__
         (  - -) zzz...
         /    ~ \   
        /_____/  U
        """)
    elif mood == "hungry":
        print(r"""
          / \__
         (  o o)  *stomach rumbles* 🍖?
         /    O \   
        /_____/  U
        """)
    else:
        print(r"""
          / \__
         (  ^.^)  
         /     \   
        /_____/ U
        """)


def check_mood():
    """Calculates pet mood based on current stats."""
    if pet["energy"] < 25:
        return "sleepy"
    elif pet["hunger"] > 70:
        return "hungry"
    elif pet["happiness"] > 80:
        return "ecstatic"
    else:
        return "normal"


def show_pet_status():
    """Displays current pet status bars."""
    mood = check_mood()
    draw_pet(mood)
    print("=" * 45)
    print(f"🐾 {pet['name']} the {pet['species']} | Mood: {mood.upper()}")
    print("=" * 45)
    print(f"🍖 Hunger:      {pet['hunger']}/100    (Lower is better)")
    print(f"💖 Happiness:   {pet['happiness']}/100 (Higher is better)")
    print(f"⚡ Energy:      {pet['energy']}/100    (Higher is better)")
    print(f"✨ Cleanliness: {pet['cleanliness']}/100")
    print(f"🎪 Tricks:      {', '.join(learned_tricks)}")
    print(f"🎖️ Badges:      {', '.join(unlocked_achievements)}")
    print("=" * 45)


# --- CARE FUNCTIONS ---

def feed_pet():
    """Feeds the pet delicious snacks."""
    print("\n🍗 Snacks Menu:")
    print("1. Crunchy Biscuit (-20 Hunger, +5 Happiness)")
    print("2. Magic Steak     (-50 Hunger, +20 Happiness)")
    print("3. Broccoli        (-10 Hunger, -5 Happiness 🥦)")

    food_choice = input("Select snack (1-3): ").strip()
    if food_choice == "1":
        pet["hunger"] = max(0, pet["hunger"] - 20)
        pet["happiness"] = min(100, pet["happiness"] + 5)
        print(f"😋 {pet['name']} munched the biscuit happily!")
    elif food_choice == "2":
        pet["hunger"] = max(0, pet["hunger"] - 50)
        pet["happiness"] = min(100, pet["happiness"] + 20)
        print(f"🥩 *Gulp!* {pet['name']} devoured the Magic Steak!")
    elif food_choice == "3":
        pet["hunger"] = max(0, pet["hunger"] - 10)
        pet["happiness"] = max(0, pet["happiness"] - 5)
        print(f"🥦 {pet['name']} made a funny face but ate the broccoli.")
    else:
        print("❓ That food isn't in the pantry!")


def play_minigame():
    """Play a fun mini guessing game with your pet to boost happiness!"""
    if pet["energy"] < 20:
        print(f"😴 {pet['name']} is too tired to play! Let them sleep first.")
        return

    print(f"\n🎾 Fetch Time! Guess which hand hides the tennis ball!")
    correct_hand = random.choice(["left", "right"])
    guess = input("Which hand? (left/right): ").strip().lower()

    if guess == correct_hand:
        print(f"🎉 Correct! {pet['name']} caught the ball in mid-air!")
        pet["happiness"] = min(100, pet["happiness"] + 25)
        pet["energy"] = max(0, pet["energy"] - 15)
        pet["hunger"] = min(100, pet["hunger"] + 10)
    else:
        print(f"😅 {pet['name']} chased after a butterfly instead!")
        pet["happiness"] = min(100, pet["happiness"] + 10)
        pet["energy"] = max(0, pet["energy"] - 10)


def teach_trick():
    """Teaches a new trick to the pet."""
    new_trick = input("\n🎪 Enter the name of a new trick to teach (e.g. Backflip, Roll Over): ").strip().title()
    if new_trick in learned_tricks:
        print(f"🐾 {pet['name']} already knows how to do '{new_trick}'!")
    elif len(new_trick) > 0:
        learned_tricks.append(new_trick)
        pet["happiness"] = min(100, pet["happiness"] + 15)
        if len(learned_tricks) >= 4:
            unlocked_achievements.add("Master Trainer")
            print("🎖️ BADGE UNLOCKED: [Master Trainer]!")
        print(f"✨ Amazing! {pet['name']} learned how to [{new_trick}]!")


def sleep_pet():
    """Puts the pet to bed to restore energy."""
    print(f"\n💤 Shhh... {pet['name']} curled up into a ball and went to sleep.")
    pet["energy"] = 100
    pet["hunger"] = min(100, pet["hunger"] + 20)
    print(f"⚡ Energy fully restored to 100%!")


# --- MAIN SIMULATOR LOOP ---

def main():
    print("========================================")
    print("🐾 WELCOME TO CYBERPET SIMULATOR 🐾")
    print("========================================")

    pet_name = input("Give your pet a name: ").strip()
    if pet_name:
        pet["name"] = pet_name

    pet_species = input("What kind of creature is it? (e.g. Dragon, Kitty, Robot): ").strip()
    if pet_species:
        pet["species"] = pet_species

    running = True
    while running:
        show_pet_status()
        print("\nWhat would you like to do?")
        print("1. 🍖 Feed Snack")
        print("2. 🎾 Play Fetch Mini-Game")
        print("3. 🎪 Teach a New Trick")
        print("4. 💤 Put Pet to Sleep")
        print("5. 🚪 Exit Game")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            feed_pet()
        elif choice == "2":
            play_minigame()
        elif choice == "3":
            teach_trick()
        elif choice == "4":
            sleep_pet()
        elif choice == "5":
            print(f"\n👋 Goodbye! {pet['name']} will miss you!")
            running = False
        else:
            print("❓ Invalid choice. Please pick 1 through 5.")


if __name__ == "__main__":
    main()

