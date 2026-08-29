"""
Lesson 08 Challenge: Secret Agent Badge & Map Coordinate Tracker!
=================================================================
MISSION 1: Map Coordinates (Tuples)
Define secret base coordinates as a tuple, unpack them into x and y,
and calculate the distance to target!

MISSION 2: Badge Deduplication & Shared Gadgets (Sets)
Eliminate duplicate gadgets from an inventory log, and find which gadgets
both Agent 007 and Agent Shadow carry!
"""

print("========================================")
print("📍 MISSION 1: SECRET BASE COORDINATES")
print("========================================")

# TODO 1: Create a tuple named base_coordinates with (x, y) coordinates like (45, 90)
base_coordinates = (0, 0)

# TODO 2: Unpack base_coordinates into two variables: base_x and base_y
base_x = 0
base_y = 0

print(f"Secret Base located at X: {base_x}, Y: {base_y}")


print("\n========================================")
print("🛡️ MISSION 2: SPY GADGET SETS")
print("========================================")

# A messy list of gadgets picked up during missions (contains duplicates!)
raw_gadget_log = ["Grappling Hook", "Laser Watch", "Smoke Bomb", "Grappling Hook", "Laser Watch", "Night Goggles"]

# TODO 3: Convert raw_gadget_log into a set named unique_gadgets to remove duplicates!
unique_gadgets = set()
print("Cleaned Gadget Inventory:", unique_gadgets)

# Agent Inventories
agent_alpha_gadgets = {"Laser Watch", "Grappling Hook", "EMP Blaster"}
agent_beta_gadgets = {"Grappling Hook", "Smoke Bomb", "Disguise Kit", "Laser Watch"}

# TODO 4: Find the gadgets that BOTH agents have in common using intersection (&).
common_gadgets = set()
print(f"Gadgets both agents have in common: {common_gadgets}")

# TODO 5: Find all unique gadgets between both agents combined using union (|).
all_gadgets = set()
print(f"Total gadget arsenal combined: {all_gadgets}")
