# 🎒 Lesson 04: The Hero's Backpack (Lists & Indexing)

What is a hero without a backpack to carry swords, potions, shields, and spell scrolls?

So far, our variables could only hold **one** item at a time (`sword = "Excalibur"`).
In this lesson, you will unlock **Lists**—a super-container that can hold hundreds of items in an organized row!

---

## 📦 1. Creating a List

A list uses square brackets `[` and `]`, with items separated by commas:

```python
backpack = ["Wooden Sword", "Health Potion", "Torch", "Magic Map"]
print(backpack)
```

---

## 🔢 2. The Golden Rule of Indexing: Start at 0!

Computers count starting from **0**, not 1! Think of list items like slots in your inventory numbered `0, 1, 2, 3...`

```text
  ["Wooden Sword", "Health Potion", "Torch", "Magic Map"]
         0               1            2          3
```

- `backpack[0]` -> `"Wooden Sword"` *(First item!)*
- `backpack[1]` -> `"Health Potion"` *(Second item!)*
- `backpack[-1]` -> `"Magic Map"` *(Negative index gives the LAST item!)*

---

## 🛠️ 3. Backpack Superpowers (List Methods)

| Spell / Method | What it Does | Example Code |
| :--- | :--- | :--- |
| **`len(list)`** | Counts how many items are in the list | `len(backpack)` -> `4` |
| **`.append(item)`** | Adds an item to the END of the backpack | `backpack.append("Dragon Shield")` |
| **`.insert(index, item)`** | Places an item at a specific slot | `backpack.insert(0, "Diamond Helmet")` |
| **`.remove(item)`** | Removes an item by name | `backpack.remove("Torch")` |
| **`.pop()`** | Removes and drops the LAST item | `dropped_item = backpack.pop()` |
| **`in` operator** | Checks if an item is in the backpack | `if "Health Potion" in backpack:` |

---

## 🎮 Hands-on Missions

1. Run [`examples.py`](examples.py) to manage your inventory!
2. Open [`challenge.py`](challenge.py) and solve the **RPG Inventory & Potion Brewer**!
3. Check [`solutions/challenge_solution.py`](solutions/challenge_solution.py) when needed.

---

## 🏅 Badge to Unlock
Earn the **🎒 Loot Collector Badge** once you manage your inventory like a pro!
