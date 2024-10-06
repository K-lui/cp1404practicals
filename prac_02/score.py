"""
CP1404/CP5632 - Practical
Refactor determine score status program to use function
"""

import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    calculate_result(score)
    result = calculate_result(score)
    print(f"Your score is {result}")

    score = random.randint(0, 100)
    calculate_result(score)
    result = calculate_result(score)
    print(f"Your random score {score} is {result}")


def calculate_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

