"""
Lesson 04: The Hero's Backpack (Lists) - Code Examples
Run this file to see how lists store, add, and remove items!
"""

print("--- 🎒 Step 1: Inspecting the Backpack ---")
inventory = ["Iron Dagger", "Health Potion", "Rope", "Gold Coin"]
print("Full Inventory:", inventory)
print("Number of items:", len(inventory))

# Accessing items using 0-based index
first_item = inventory[0]
second_item = inventory[1]
last_item = inventory[-1]

print(f"Slot 0 (First Item): {first_item}")
print(f"Slot 1 (Second Item): {second_item}")
print(f"Slot -1 (Last Item): {last_item}")


print("\n--- 🗡️ Step 2: Finding Loot & Updating Items ---")
# Modifying an existing slot (Upgrading the dagger to a Flame Sword!)
inventory[0] = "Flame Sword"
print("Upgraded Slot 0:", inventory)

# Adding new loot to the end of the list
inventory.append("Invisibility Cloak")
print("Found new loot! Inventory is now:", inventory)


print("\n--- 🧪 Step 3: Using & Dropping Items ---")
# Checking if an item exists
if "Health Potion" in inventory:
    print("✨ Found Health Potion! Drinking it to restore HP...")
    inventory.remove("Health Potion")
    print("Drank potion. Inventory remaining:", inventory)

# Dropping the last item with pop()
dropped = inventory.pop()
print(f"Dropped {dropped} to make room for heavier armor!")
print("Final Backpack State:", inventory)

