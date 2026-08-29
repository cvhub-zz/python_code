"""
Lesson 08 Challenge Solution: Secret Agent Coordinates & Gadgets!
"""

print("========================================")
print("📍 MISSION 1: SECRET BASE COORDINATES")
print("========================================")

base_coordinates = (45, 90)
base_x, base_y = base_coordinates

print(f"Secret Base located at X: {base_x}, Y: {base_y}")


print("\n========================================")
print("🛡️ MISSION 2: SPY GADGET SETS")
print("========================================")

raw_gadget_log = ["Grappling Hook", "Laser Watch", "Smoke Bomb", "Grappling Hook", "Laser Watch", "Night Goggles"]

unique_gadgets = set(raw_gadget_log)
print("Cleaned Gadget Inventory:", unique_gadgets)

agent_alpha_gadgets = {"Laser Watch", "Grappling Hook", "EMP Blaster"}
agent_beta_gadgets = {"Grappling Hook", "Smoke Bomb", "Disguise Kit", "Laser Watch"}

common_gadgets = agent_alpha_gadgets & agent_beta_gadgets
print(f"Gadgets both agents have in common: {common_gadgets}")

all_gadgets = agent_alpha_gadgets | agent_beta_gadgets
print(f"Total gadget arsenal combined: {all_gadgets}")

exclusive_alpha = agent_alpha_gadgets - agent_beta_gadgets
print(f"Gadgets only Alpha has: {exclusive_alpha}")

