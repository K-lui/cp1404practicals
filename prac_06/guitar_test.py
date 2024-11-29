"""
CP1404 Practical 06 - Guitar Test

Guitar Test
Estimate: 120 minutes
Actual:    38 minutes
"""

from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013)
# guitars = [guitar1, guitar2]
# for guitar in guitars:
print(f"{guitar1.name} get_age() - Expected 100.", guitar1.get_age(current_year=2022))
print(f"{guitar2.name} get_age() - Expected 9.", guitar2.get_age(current_year=2022))
print(f"{guitar1.name} is_vintage() - Expected True.", guitar1.is_vintage())
print(f"{guitar2.name} is_vintage() - Expected False.", guitar2.is_vintage())




