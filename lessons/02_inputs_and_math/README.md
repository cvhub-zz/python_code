# 💬 Lesson 02: Secret Inputs & Math Spells

In Lesson 01, Python talked to us. But what if we want Python to ask questions and listen to our answers? 

In this lesson, you will learn:
1. **`input()`**: How to ask the player questions and save their answers.
2. **The f-String Power**: How to mix variables into text seamlessly like magic!
3. **Math Spells**: How Python can calculate sums, slice pizzas, and find remainders.

---

## 👂 1. Listening to the Player with `input()`

The `input()` spell pauses the program and waits for the player to type something and press **Enter**.

```python
player_name = input("What is your wizard name? ")
print("Welcome to the Academy,", player_name)
```

---

## ✨ 2. The f-String Superpower (`f"..."`)

Instead of writing lots of commas in `print()`, you can put an `f` before quotes and put variable names inside curly braces `{}`!

```python
score = 250
lives = 3
print(f"Player {player_name} has {score} points and {lives} lives left!")
```

---

## ➗ 3. Python Math Spells

Python is a super-calculator:

| Spell | Symbol | Example | Result |
| :--- | :---: | :---: | :---: |
| **Add** | `+` | `10 + 5` | `15` |
| **Subtract** | `-` | `10 - 3` | `7` |
| **Multiply** | `*` | `4 * 3` | `12` |
| **Divide** | `/` | `10 / 2` | `5.0` |
| **Integer Divide (No Decimals)** | `//` | `11 // 2` | `5` |
| **Modulo (Remainder)** | `%` | `11 % 2` | `1` |

### ⚠️ The Secret `input()` Trap: Words vs. Numbers!
Whenever someone types into `input()`, Python sees it as **text (String)**.
- `"5" + "5"` becomes `"55"` (gluing words together!).
- To make Python do real math, wrap the input with `int()`:

```python
# Convert text to a whole number integer:
slices = int(input("How many slices of pizza? "))
friends = int(input("How many friends? "))
slices_each = slices // friends
leftovers = slices % friends
print(f"Each friend gets {slices_each} slices, with {leftovers} slice(s) left for the dog! 🐶")
```

---

## 🎮 Hands-on Missions

1. Run [`examples.py`](examples.py) to play with interactive input and math!
2. Open [`challenge.py`](challenge.py) and solve the **Pizza Party Calculator & Mad Libs Story**!
3. Check [`solutions/challenge_solution.py`](solutions/challenge_solution.py) if you need help.

---

## 🏅 Badge to Unlock
Earn the **🧪 Math Alchemist Badge** when your pizza party calculator runs!
