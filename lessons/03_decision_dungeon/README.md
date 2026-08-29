# 🏰 Lesson 03: Decision Dungeon (If / Elif / Else)

Imagine standing in front of two spooky iron doors in a dark dungeon.
- **IF** you open the left door, you find a chest filled with diamonds! 💎
- **ELSE IF** you open the right door, a fire-breathing dragon roars! 🐉
- **ELSE**, you stay in the hallway where it's safe.

In this lesson, you will teach Python how to make smart choices using `if`, `elif`, and `else`!

---

## ⚖️ 1. Comparison Detective Symbols

Python has special symbols to compare values:

| Symbol | Meaning | Example | Result |
| :---: | :--- | :---: | :---: |
| `==` | Is Equal To? *(Double equals!)* | `5 == 5` | `True` |
| `!=` | Is NOT Equal To? | `5 != 3` | `True` |
| `>` | Greater than | `10 > 3` | `True` |
| `<` | Less than | `2 < 8` | `True` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |
| `<=` | Less than or equal to | `4 <= 5` | `True` |

> ⚠️ **Common Trap**: A single `=` puts something into a variable box (`score = 10`). A double `==` asks a question (`score == 10`).

---

## 🔀 2. The Decision Tree (`if`, `elif`, `else`)

```python
door = input("Choose door (left/right): ")

if door == "left":
    print("💎 You found the Diamond Vault!")
elif door == "right":
    print("🐉 Oh no! A dragon sneezed flames at you!")
else:
    print("❓ You stood still, confused by the doors.")
```

### 🚪 Indentation Rule
Notice the 4 spaces (or Tab) before the `print` lines inside the `if` blocks! This indentation tells Python: *"Only run this code if this specific door was chosen!"*

---

## 🔗 3. Combining Clues with `and`, `or`, `not`

- **`and`**: BOTH conditions must be True.
  ```python
  if has_key and level >= 5:
      print("You can unlock the Boss Chamber!")
  ```
- **`or`**: At least ONE condition must be True.
  ```python
  if is_wizard or has_magic_scroll:
      print("You can read the glowing ancient runes!")
  ```
- **`not`**: Flips True to False, and False to True.
  ```python
  if not is_poisoned:
      print("You feel healthy and energized!")
  ```

---

## 🎮 Hands-on Missions

1. Run [`examples.py`](examples.py) to explore decision logic.
2. Open [`challenge.py`](challenge.py) and code your own interactive **Haunted Castle Escape**!
3. Need a peek at the answer? Check [`solutions/challenge_solution.py`](solutions/challenge_solution.py).

---

## 🏅 Badge to Unlock
Earn the **🏰 Dungeon Master Badge** once your interactive adventure game works!

