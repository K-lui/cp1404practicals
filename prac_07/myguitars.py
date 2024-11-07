"""
CP1404/CP5632 Practical
Intermediate Exercises - More Guitars!
"""

import csv

from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Open the file for reading
    read_file(guitars)
    # Sort guitars list by year
    guitars = sorted(guitars)

    # Loop through and display all guitars from guitars list
    for guitar in guitars:
        print(guitar)


def read_file(guitars):
    """Read and format file"""
    in_file = open('guitars.csv', 'r')
    # File is formatted: Name,Year,Cost
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        part = line.strip().split(',')
        guitar = Guitar(part[0], int(part[1]), float(part[2]))
        # Add the guitar we've constructed to this list
        guitars.append(guitar)
    in_file.close()


main()














