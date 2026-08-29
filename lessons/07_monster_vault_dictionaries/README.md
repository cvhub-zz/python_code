# 🗝️ Lesson 07: Monster Vault (Dictionaries)

Lists are great when items are in a row (`[0, 1, 2]`), but what if you want to look up something by its **label** or **name** instead of a number?

Enter **Dictionaries**! In a real dictionary, you look up a **Word** (Key) to find its **Definition** (Value).
In Python, a dictionary maps **Keys** to **Values**:

```python
player = {
    "name": "Luna",
    "class": "Mage",
    "health": 100,
    "mana": 50,
    "gold": 250
}
```

---

## 🔑 1. Reading & Changing Dictionary Values

Use square brackets with the key name:

```python
# Reading a value
print(player["name"])    # Prints: Luna
print(player["health"])  # Prints: 100

# Changing an existing value
player["health"] = 90

# Adding a brand new key-value pair!
player["pet"] = "Shadow Fox"
```

---

## 🛡️ 2. Safe Lookups with `.get()`

If you ask for a key that doesn't exist (like `player["super_shield"]`), Python will throw an error and crash!
To avoid crashes, use `.get()` with a safe default fallback:

```python
shield = player.get("shield", "No shield equipped")
print(shield)  # Prints: No shield equipped
```

---

## 🔄 3. Looping through a Dictionary with `.items()`

You can inspect all keys and values in a single loop:

```python
for key, value in player.items():
    print(f"🔹 {key.capitalize()}: {value}")
```

---

## 🎮 Hands-on Missions

1. Run [`examples.py`](examples.py) to inspect the Monster Vault!
2. Open [`challenge.py`](challenge.py) and build your **Pokédex / Monster Encyclopedia**!
3. Check [`solutions/challenge_solution.py`](solutions/challenge_solution.py) when needed.

---

## 🏅 Badge to Unlock
Earn the **🗝️ Vault Keeper Badge** once your monster lookup system works smoothly!

