"""
CP1404/CP5632 Practical
Emails Program
"""

"""
Emails
Estimate: 60 minutes
Actual:  230 minutes
"""


def main():
    """Create a dictionary of emails and names"""
    email_to_name = {}
    user_email = input('Email: ')
    while user_email != "":
        name_of_user = extract_name_from_email(user_email)
        answer = input(f"Is your name {name_of_user.title()}? (Y/n) ").lower()
        if answer == "y" or answer == "yes":
            email_to_name[user_email] = name_of_user
        else:
            name_of_user = input("Name: ")
            email_to_name[user_email] = name_of_user
        user_email = input('Email: ')

    for user_email, name_of_user in email_to_name.items():
        print(f"{name_of_user.title()} ({user_email})")


def extract_name_from_email(user_email):
    """Extract name from given email"""
    break_up_email = user_email.split('@')
    strings_in_email = [word.replace(".", " ") for word in break_up_email]
    return strings_in_email[0]


main()
