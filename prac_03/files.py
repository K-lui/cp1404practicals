"""
CP1404/CP5632 - Practical
files D0-from-scratch Exercises
"""


FILENAME = "name"

# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use
# open and close for this question.
name_file = FILENAME
out_file = open(name_file, 'w')

name = input('Enter name: ')
out_file.write(name)

out_file.close()


# 2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as
# above) then prints (note the exact output),
in_file = open(name_file, 'r')
print(in_file.read())

in_file.close()


# 3. Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result,
# which should be... 59. Use with instead of open and close for this question.
with open("numbers.txt", 'r') as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
print(f"{number_1} + {number_2}: {number_1 + number_2}")


# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file
# with any number of numbers. Use with instead of open and close for this question.
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        print(line, end='')
