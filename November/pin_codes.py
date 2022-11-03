from pickle import FALSE


pin = "1234"
pin_two = "-12345"
pin_three = "1.234"
pin_five = "00000000"


def validate_pin(pin):
    if len(pin) != 4 or len(pin) != 6:
        return False
    else:
        for char in pin:
            print(char)

        #return true or fals

validate_pin(pin_five)