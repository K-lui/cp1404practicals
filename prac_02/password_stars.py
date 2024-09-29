
PASSWORD = "apple"

key = input("Enter password: ")
while key != PASSWORD:
    print("Wrong password!")
    key = input("Enter password: ")
length = PASSWORD
print("correct!")
for i in range(len(length)):
    print("*", end="")
