"""
CP1404 Practical 06 - Programming Language


Programming Language
Estimate: 120 minutes
Actual:    32 minutes
"""


from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# print(python) # Ignore this line
languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for row in languages:
    if row.is_dynamic():
        print(row.name)
