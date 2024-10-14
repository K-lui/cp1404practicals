"""
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

numbers = [3, 1, 4, 1, 5, 9, 2]
"""


# 3
# 2
# 1
# 3, 1, 4, 1, 5, 9
# 1
# true
# false
# false
# 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

"""
1. Change the first element of numbers to "ten" (the string, not the number 10)
2. Change the last element of numbers to 1
3. Print all the elements from numbers except the first two (slice)
4. Print whether 9 is an element of numbers"""

numbers = [3, 1, 4, 1, 5, 9, 2]


# 1.
del numbers[0]
numbers.insert(0, "ten")
print(numbers)


# 2.
del numbers[-1]
numbers.append(1)
print(numbers)


# 3.
print(numbers[2:10])


# 4.
print(9 in numbers)
