"""
Cp1404 - Band class
"""


class Band:

    def __init__(self, name="", ):
        self.name = name
        self.musicians = []
        self.instruments = []

    def __str__(self):
        return f"{self.name} {self.musicians}"

    def add(self, member):
        self.musicians.append(member)

    def play(self):
        plays = [member.play() for member in self.musicians]
        return f"{"\n".join(plays)}"



