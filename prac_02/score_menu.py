"""
CP1404 Practical 2 - Menu
"""


import random


MENU = "(G)et a valid score(0-100)\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    score = 0
    choice = input(">>>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Your score is {score}")
        elif choice == "P":
            result = calculate_result(score)
            print(f"{score} is: {result}")
        elif choice == "S":
            determine_stars(score)
        print(MENU)
        choice = input(">>>> ").upper()
    print("See ya!")


def get_valid_score():
    score = random.randint(1, 100)
    return score


def calculate_result(score):
    if score >= 90:
        return "Excellent!"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def determine_stars(score):
    print(f"{score} stars")
    print("*" * score)


main()
