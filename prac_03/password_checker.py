"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

import string

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if str.islower(character):
            number_of_lower = number_of_lower + 1
        if str.isupper(character):
            number_of_upper = number_of_upper + 1
        if str.isdigit(character):
            number_of_digit = number_of_digit + 1
        if IS_SPECIAL_CHARACTER_REQUIRED is True:
            number_of_special = number_of_special + 1
            if SPECIAL_CHARACTERS is False:
                return False
    if number_of_digit == 0 or number_of_lower == 0 or number_of_upper == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
