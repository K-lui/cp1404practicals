"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Project Management Program



Project Management Program
Estimate: 120 minutes
Actual: 600 minutes
"""

import datetime
from prac_07.project import Project

FILENAME = "projects.txt"
MENU = ("(L) - Load Projects\n"
        "(S) - Save Projects\n"
        "(D) - Display Projects\n"
        "(F) - Filter Projects by date\n"
        "(A) - Add new Project\n"
        "(U) - Update Project\n"
        "(Q) - Quit\n")

incomplete_projects = []
complete_projects = []
in_file = open(FILENAME, 'r')
in_file.readline()
for line in in_file:
    part = line.strip().split("\t")
    date = datetime.datetime.strptime(part[1], '%d/%m/%Y')
    project = Project(part[0], date, int(part[2]), float(part[3]), int(part[4]))
    if int(part[4]) != 100:
        incomplete_projects.append(project)
    else:
        complete_projects.append(project)
in_file.close()

print("Welcome to Pythonic Project Management")
number_of_project = len([line for line in incomplete_projects + complete_projects])
print(f"Loaded {number_of_project} projects from {FILENAME}")

print(MENU)

option = input(">>> ").upper()
while option != "Q":
    if option == "L":
        load_project = input("Enter a file name: ")
        with open(load_project, "r") as load_project:
            load_project.readline()
            for line in load_project:
                line = line.strip().split("\t")
                print(f'{line[0]} {line[1]}, {line[2]}, ${line[3]:}, {line[4]}%')
            print(MENU)
            option = input(">>> ").upper()

    elif option == "S":
        save_project = input("Enter a file name: ")
        with open(save_project, "w") as out_file:
            projects = incomplete_projects + complete_projects
            out_file.write(f"Name\tStart Date\tPriority\tCost Estimation\tCompletion Percentage\n")
            for line in projects:
                formatted_date = line.start_date.strftime("%d/%m/%Y")
                out_file.write(f"{line.name}\t{formatted_date}\t{line.priority}\t{line.cost}\t{line.completion}\n")
            print(MENU)
            option = input(">>> ").upper()

    elif option == "D":
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(" ", project)
        print("Completed projects:")
        for project in complete_projects:
            print(" ", project)
        print(MENU)
        option = input(">>> ").upper()

    elif option == "F":
        date_input = input("Show projects that start after date (dd/mm/yyyy): ")
        start_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
        for project in incomplete_projects:
            if project.is_later_than(start_date):
                print(project)
        print(MENU)
        option = input(">>> ").upper()

    elif option == "A":
        print("Let's add a new project")
        name = input("Name: ")
        new_start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), '%d/%m/%Y')
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        new_project = (Project(name, new_start_date, priority, cost, completion))
        if completion == 100:
            complete_projects.append(new_project)
        else:
            incomplete_projects.append(new_project)
        print(MENU)
        option = input(">>> ").upper()

    elif option == "U":
        for index, project in enumerate(incomplete_projects + complete_projects):
            print(index, project)
        choice = int(input("Project choice: "))
        for index, project in enumerate(incomplete_projects + complete_projects):
            if choice == index:
                print(project)
                new_percentage = int(input("New Percentage: "))
                project.completion = new_percentage
                new_priority = input("New Priority: ")
                if new_priority != "":
                    project.priority = int(new_priority)
                project.priority = project.priority
                if project.completion == 100:
                    complete_projects.append(project)
                    incomplete_projects.remove(project)
                elif project.completion < 100:
                    incomplete_projects.append(project)
                    if project in complete_projects:
                        complete_projects.remove(project)
                    incomplete_projects.remove(project)
        print(MENU)
        option = input(">>> ").upper()
answer = input(f"Would you like to save to {FILENAME}? ").lower()
if answer == "no" or answer == "nah":
    print("Thank you for using custom-built project management software.")

else:
    with open(FILENAME, "w") as out_file:
        projects = incomplete_projects + complete_projects
        out_file.write(f"Name\tStart Date\tPriority\tCost Estimation\tCompletion Percentage\n")
        for line in projects:
            formatted_date = line.start_date.strftime("%d/%m/%Y")
            out_file.write(f"{line.name}\t{formatted_date}\t{line.priority}\t{line.cost}\t{line.completion}\n")
        print("saved...")

