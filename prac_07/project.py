class Project:

    def __init__(self, name, start_date, priority=0, cost=0, completion=""):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        formatted_date = self.start_date.strftime("%m/%d/%Y")
        return (f'{self.name}, start: {formatted_date}, priority {self.priority}, estimate: ${self.cost},'
                f' completion: {self.completion}%')

    def is_later_than(self, start_date):
        return self.start_date.date() >= start_date

