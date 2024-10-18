"""
CP1404/CP5632 Practical
Emails Program
"""

"""
Emails
Estimate: 60 minutes
Actual:  227 minutes
"""

EMAIL_TO_NAMES = {}


def main():
    user_email = input('Email: ')
    while user_email != "":
        name_of_user = extract_name_from_email(user_email)

        # for name_of_user in strings_in_email:
        answer = input(f"Is your name {name_of_user.title()}? (Y/n) ").lower()
        if answer == "y" or answer == "yes":
            EMAIL_TO_NAMES[user_email] = name_of_user
        else:
            name_of_user = input("Name: ")
            EMAIL_TO_NAMES[user_email] = name_of_user
        user_email = input('Email: ')

    for user_email, name_of_user in EMAIL_TO_NAMES.items():
        print(f"{name_of_user.title()} ({user_email})")


def extract_name_from_email(user_email):
    break_up_email = user_email.split('@')
    strings_in_email = [word.replace(".", " ") for word in break_up_email]
    return strings_in_email[0]


main()
