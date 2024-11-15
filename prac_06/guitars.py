"""
CP1404 Practical 06 - Guitars (The client program)

Guitars
Estimate: 60 minutes
Actual:  123 minutes
"""

from prac_06.guitar import Guitar

guitars = []

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added.\n")
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    name_width = max([len(guitar.name) for guitar in guitars])
    cost_width = max([len(str(guitar.cost)) for guitar in guitars])
    guitar.get_age(2022)
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}:  {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:>{cost_width + 2},.2f} "
          f"{vintage_string}")





