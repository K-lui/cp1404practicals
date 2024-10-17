"""
CP1404/CP5632 Practical
Hex colours Program
"""

COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Aqua": "#00ffff", "Beige":
    "#f5f5dc", "Black": "#000000", "Blond": "#faf0be", "Bone": "#e3dac9", "Corn": "#fbec5d", "Cream": "#fffdd0"}
print(COLOUR_TO_CODE)

state_code = input("Enter short state: ").lower()
while state_code != "":
    try:
        print(state_code, "is", COLOUR_TO_CODE[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").lower()
# for state_code in COLOUR_TO_CODE:
#     print(f"{state_code:4} is {COLOUR_TO_CODE[state_code]}")
