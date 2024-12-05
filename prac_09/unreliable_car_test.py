"""
CP1404 - Unreliable Car test
"""

from prac_09.unreliable_car import UnreliableCar


def main():

    good_car = UnreliableCar("Good", 100, 90)
    bad_car = UnreliableCar("Bad", 100, 9)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")
    print(good_car)
    print(bad_car)


main()


