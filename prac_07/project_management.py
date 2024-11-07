"""
CP1404/CP5632 Practical
Do-from-scratch Exercises - Project Management Program



Project Management Program
Estimate: 120 minutes
Actual:
"""


import datetime
from prac_07.project import Project

incomplete_projects = []
complete_projects = []
menu = ("(L) - Load Projects\n"
        "(S) - Save Projects\n"
        "(D) - Display Projects\n"
        "(F) - Filter Projects by date\n"
        "(A) - Add new Project\n"
        "(U) - Update Project\n"
        "(Q) - Quit\n")

in_file = open('projects.txt', 'r')
in_file.readline()
for line in in_file:
    part = line.strip().split("\t")
    date = datetime.datetime.strptime(part[1], '%d/%m/%Y')
    project = Project(part[0], date, int(part[2]), float(part[3]), part[4])
    if line[4] != "100":
        incomplete_projects.append(project)
    else:
        complete_projects.append(project)
in_file.close()

print("Welcome to Pythonic Project Management")
print(menu)

option = input(">>> ").upper()
if option == "L":
    load_project = input("Enter a file name: ")
    with open(load_project, "r") as load_project:
        for line in load_project:
            line = line.strip().split("\t")
            print(f'{line[0]:>18}: {line[1]} ({line[2]}) ${line[3]:<10} {line[4]}%')

elif option == "S":
    save_project = input("Enter a file name: ")
    with open(save_project, "w") as save_project:
        for project in incomplete_projects:
            save_project.write(str(project))

elif option == "D":
    print("Incomplete projects:")
    for project in incomplete_projects:
        if project.completion != "100":
            print(" ", project)
    print("Completed projects:")
    for project in incomplete_projects:
        if project.completion == "100":
            print(" ", project)

elif option == "F":
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    for project in incomplete_projects:
        if project.is_later_than(start_date):
            print(project)

elif option == "A":
    print("Let's add a new project")
    name = input("Name: ")
    new_start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    incomplete_projects = [Project(name, new_start_date, priority, cost, completion)]

elif option == "U":
    for index, project in enumerate(incomplete_projects):
        print(index, project)
    choice = int(input("Project choice: "))
    for index, project in enumerate(incomplete_projects):
        if choice == index:
            new_project = project
            print(new_project)
            new_percentage = int(input("New Percentage: "))
            new_project.completion = new_percentage
            project.completion = new_project.completion

# for project in projects:
#     print(project)











