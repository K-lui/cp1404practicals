class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=True or False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return languages that are dynamic"""
        if self.typing == "Dynamic":
            return {self.typing}








