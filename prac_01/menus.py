"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message"""

name = input("Enter your name: ")
print("(H) Hello\n(G) Goodbye\n(Q) Quit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print("(H) Hello\n(G) Goodbye\n(Q) Quit")
    choice = input(">>> ").upper()
print("Finished.")
