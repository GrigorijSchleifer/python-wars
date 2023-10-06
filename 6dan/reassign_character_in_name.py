# This should change the character on a specified position of the name
def exchange_namechars():
    while True:
        try:
            name = str(input("What is your name: \n"))
            break
        except ValueError:
            print("Only strings are allowed")
    for i in name:
        index = 0
        print(f"{index}: is {i} \n")

exchange_namechars()

