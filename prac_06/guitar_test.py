"""
CP1404 Practical 06 - Guitar Test

Programming Language
Estimate: 120 minutes
Actual:       minutes
"""

from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013)
guitars = [guitar1, guitar2]
# print(f"My guitar: {name}, first made in {year}")
# print(f"{name} ({year}) : ${cost:,.2f}")
for guitar in guitars:
    print(guitar.get_age(current_year=2022))
    print(guitar.is_vintage())




