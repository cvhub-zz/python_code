"""
Lesson 05: Time Loops & Repeaters - Code Examples
Run this file to see for-loops and while-loops in action!
"""

print("--- 🚀 Example 1: Rocket Countdown (for loop with range) ---")
# range(start, stop, step): starts at 5, goes down to 1 by subtracting 1 (-1)
for second in range(5, 0, -1):
    print(f"T-minus {second}...")
print("🚀 BLAST OFF INTO SPACE!\n")


print("--- 🍕 Example 2: Serving Pizza Slices (for loop over list) ---")
party_guests = ["Maya", "Leo", "Sam", "Zoe"]
for guest in party_guests:
    print(f"🍕 Here is a warm slice of pizza for {guest}!")


print("\n--- 🪙 Example 3: Coin Collector (while loop) ---")
piggy_bank = 0
goal = 5

while piggy_bank < goal:
    piggy_bank += 1    # Shortcut for: piggy_bank = piggy_bank + 1
    print(f"Clink! Dropped a coin into the bank. Total coins: {piggy_bank}")

print("🎉 Goal reached! Time to buy a comic book!\n")


print("--- 🔐 Example 4: Secret Door Code (while loop with break) ---")
correct_pin = "777"
attempts = 0

while attempts < 3:
    pin = input("Enter 3-digit PIN: ")
    if pin == correct_pin:
        print("🔓 ACCESS GRANTED! Vault opened!")
        break
    else:
        attempts += 1
        print(f"❌ Invalid PIN. Attempts remaining: {3 - attempts}")

if attempts == 3:
    print("🚨 ALARM! Security locked down!")
