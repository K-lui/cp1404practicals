"""
CP1404/CP5632 Practical
Hex colours Program
"""

COLOUR_TO_CODE = {"aliceblue": "#f0f8ff", "amber": "#ffbf00", "amethyst": "#9966cc", "aqua": "#00ffff", "beige":
    "#f5f5dc", "black": "#000000", "blond": "#faf0be", "bone": "#e3dac9", "corn": "#fbec5d", "cream": "#fffdd0"}
print(COLOUR_TO_CODE)

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid short state")
    colour = input("Enter short state: ").lower()
