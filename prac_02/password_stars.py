"""CP1404 - Refactoring password check program into function"""

SECRET = "apple"


def main():
    password = get_password()
    while password != SECRET:
        print("Wrong password!")
        password = get_password()
    print("correct!")
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks"""
    for i in range(len(password)):
        print("*", end="")


def get_password():
    """get password"""
    password = input("Enter password: ")
    return password


main()
