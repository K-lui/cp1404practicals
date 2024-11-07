"""
CP1404/CP5632 Practical
Intermediate Exercises - More Guitars!
"""


from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Get new guitar details from user
    name = input("New Guitar: ").title()
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    # Assign entered elements to new guitar variable
    new_guitar = Guitar(name, year, cost)
    # Add the new guitar to the list
    guitars.append(new_guitar)

    # Open the file for reading
    read_file(guitars)
    # Sort guitars list (newest to oldest)
    guitars = sorted(guitars)

    # Loop through and display all guitars from guitars list
    for guitar in guitars:
        print(guitar)
    # Open the file for appending
    append_to_file(cost, name, year)


def append_to_file(cost, name, year):
    """Add new guitar details to CSV file"""
    with open("guitars.csv", "a") as append_file:
        append_file.write(f"\n{name},{str(year)},{str(cost)}")


def read_file(guitars):
    """Read and format file"""
    in_file = open('guitars.csv', 'r')
    # File is formatted: Name,Year,Cost
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        part = line.strip().split(',')
        guitar = Guitar(part[0], int(part[1]), float(part[2]))
        # Add the guitar we've constructed to the list
        guitars.append(guitar)
    in_file.close()


main()














