# 📜 Lesson 06: Spellbooks & Magic Functions

A Master Wizard doesn't invent a new spell from scratch every time they fight a monster. They write down the spell in their **Spellbook**, give it a name, and cast it anytime with a single word!

In Python, these reusable spells are called **Functions** (`def`).

---

## 🔮 1. Creating a Simple Function

You define a function with `def`, followed by the name, parentheses `()`, and a colon `:`.

```python
def cast_fireball():
    print("🔥 WHOOSH! A blazing fireball erupts from your hands!")

# Casting the spell:
cast_fireball()
cast_fireball()
```

---

## 🧪 2. Functions with Parameters (Custom Ingredients)

You can pass ingredients (called **arguments** or **parameters**) into your function:

```python
def greet_hero(hero_name, title="The Brave"):
    print(f"🌟 Welcome, {hero_name} {title}!")

greet_hero("Arthur")              # Uses default title "The Brave"
greet_hero("Merlin", "The Wise")  # Uses custom title "The Wise"
```

---

## 🎁 3. The `return` Spell (Giving Back a Value)

Some functions do math or craft an item and **send it back** to you using `return`:

```python
def calculate_damage(base_attack, critical_hit):
    if critical_hit:
        return base_attack * 2
    else:
        return base_attack

# Capture the returned value:
total_damage = calculate_damage(50, True)
print(f"💥 Critical Strike dealt {total_damage} damage!")
```

> 💡 **Remember**: `print()` just shows text on screen, but `return` gives the result back so your code can use it in other calculations!

---

## 🎮 Hands-on Missions

1. Run [`examples.py`](examples.py) to cast different function spells.
2. Open [`challenge.py`](challenge.py) and build the **Magic Battle Spellbox**!
3. Need guidance? Check [`solutions/challenge_solution.py`](solutions/challenge_solution.py).

---

## 🏅 Badge to Unlock
Earn the **📜 Grand Sorcerer Badge** once your functions calculate damage and heal characters flawlessly!
