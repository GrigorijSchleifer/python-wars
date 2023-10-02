# This should change the character on a specified position of the name
def exchange_namechars():
    while True:
        try:
            name = input("What is your name: \n")
            # limit user to enter only real names without integers
            if name.isdigit():
                continue
        except ValueError:
            print("Only")

exchange_namechars()

