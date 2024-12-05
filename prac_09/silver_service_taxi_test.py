"""
CP1404 - Silver Service Taxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"${taxi.get_fare():.2f}")


main()


