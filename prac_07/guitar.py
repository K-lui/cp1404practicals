class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year > other.year

    def get_age(self, current_year):
        self.age = current_year - self.year
        return f"Got {self.age}"

    def is_vintage(self):
        if self.age >= 50:
            return True
        else:
            return False
