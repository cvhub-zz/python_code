# ⏳ Lesson 05: Time Loops & Repeaters (For & While Loops)

Imagine if your coach told you: *"Do 100 jumping jacks!"*
Would you want to write `print("Jumping jack!")` 100 times in your code? Of course not! 😅

Programmers use **Loops** to repeat actions automatically in milliseconds!

---

## 🔁 1. The `for` Loop: Counting & Inspecting

### 🎯 Counting with `range()`
The `range(start, stop)` function counts numbers.
> ⚠️ **Note**: `range(1, 6)` starts at 1 and stops *before* 6 (1, 2, 3, 4, 5).

```python
for count in range(1, 6):
    print(f"Blast off in {count}...")
```

### 🎒 Iterating through a List
You can visit every single item in a list with ease:

```python
monsters = ["Slime", "Skeleton", "Zombie", "Dragon"]
for m in monsters:
    print(f"⚔️ A wild {m} appears!")
```

---

## 🔄 2. The `while` Loop: Repeating Until a Goal is Met

A `while` loop keeps running as long as its condition is `True`.

```python
energy = 3

while energy > 0:
    print(f"Running! Energy left: {energy}")
    energy = energy - 1  # Reduce energy by 1

print("Tired out! Need a nap. 😴")
```

---

## 🛑 3. Escaping with `break`

If you are trapped in a loop and need to exit immediately, shout `break`!

```python
while True:
    secret_word = input("Say the password to enter: ")
    if secret_word == "Abracadabra":
        print("🔓 Access Granted!")
        break
    else:
        print("❌ Wrong password, try again!")
```

---

## 🎮 Hands-on Missions

1. Run [`examples.py`](examples.py) to watch loops in action!
2. Open [`challenge.py`](challenge.py) and code the **Secret Number Guessing Game & Rocket Countdown**!
3. Need a hint? Look at [`solutions/challenge_solution.py`](solutions/challenge_solution.py).

---

## 🏅 Badge to Unlock
Earn the **⏳ Time Bender Badge** once your guessing game loops smoothly!

