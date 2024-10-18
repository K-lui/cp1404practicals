"""
CP1404/CP5632 Practical
Emails Program
"""

"""
Emails
Estimate: 60 minutes
Actual:  204 minutes
"""

EMAIL_TO_NAMES = {}


user_email = input('Email: ')
# user_email = "kevin.lui@my.jcu.edu.au"
while user_email != "":
    break_up_email = user_email.split('@')
    strings_in_email = [word.replace(".", " ") for word in break_up_email]
    del strings_in_email[1]

    for name_of_user in strings_in_email:
        answer = input(f"Is your name {name_of_user.title()}? (Y/n) ").lower()
        if answer == "y" or answer == "yes":
            EMAIL_TO_NAMES[user_email] = name_of_user
        else:
            name_of_user = input("Name: ")
            EMAIL_TO_NAMES[user_email] = name_of_user
    user_email = input('Email: ')

for user_email, name_of_user in EMAIL_TO_NAMES.items():
    print(f"{name_of_user.title()} ({user_email})")

