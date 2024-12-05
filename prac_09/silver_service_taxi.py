"""
CP1404 - Silver Service Taxi derived from Taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall:.2f}"

    def get_fare(self):
        return self.flag_fall + super().get_fare()





