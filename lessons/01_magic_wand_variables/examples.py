"""
Lesson 01: Magic Wand & Variables - Code Examples
Run this file to see how Python prints messages and uses variables!
"""

# -------------------------------------------------------------
# 1. THE MAGIC PRINT WAND
# -------------------------------------------------------------
print("========================================")
print("✨ WELCOME TO PYTHON QUEST! ✨")
print("========================================")

# Printing text (Strings)
print("Hello, young coder! Ready to begin your journey?")

# Printing numbers (Integers and Floats)
print(100)       # Whole number (integer)
print(99.5)      # Decimal number (float)

# Printing multiple items separated by commas
print("Player Level:", 1, "Status: Ready!")


# -------------------------------------------------------------
# 2. VARIABLE BOXES
# -------------------------------------------------------------
print("\n--- 📦 Unpacking the Variable Vault ---")

character_name = "Alex the Brave"
character_class = "Knight"
health_points = 100
shield_power = 25.5
has_magic_key = True   # A Boolean: can be True or False!

print("Character Name:", character_name)
print("Class:", character_class)
print("Health Points:", health_points)
print("Shield Power:", shield_power)
print("Carrying Magic Key?:", has_magic_key)


# -------------------------------------------------------------
# 3. CHANGING (UPDATING) VARIABLES
# -------------------------------------------------------------
print("\n--- ⚔️ Battle Begins: Taking Damage! ---")

# The player takes 20 damage!
health_points = 80
print("Ouch! A wild slime attacked. Health is now:", health_points)

# The player drinks a super potion!
health_points = 100
print("Slurppp! Drank a healing potion. Health restored to:", health_points)

print("\nAwesome job! Now open challenge.py and build your superhero card!")
