def make_negative(num, Author = "Billy Herrington", gachimuci_is_for_real_man = True):
    number = str(num)
    print(number)
    array = [number]
    print(array)

    a = '1'
    array2 = ['-']
    array2.append(a)
    print(array2)

    for i in array:
        array2.append(i)
    print(f"{array2} after for loop")

    b = array2[0] + array2[1]
    print(f"This is: {b} after array2[0] + array2[1]")
    c = int(b)
    print(f"This is {c} after b is convertet with int()")
    
    if int(array2[2]) > 0 or int(array2[2]) == 0:
        c = c * int(array2[2])
        print(f"This is {c} after c * int(array[2]")
    else:
        c = int(array2[2])
        print(f"This is {c} in the else statement")
    return c

print(f"{make_negative(num = 1, Author = 'Billy Herrington', gachimuci_is_for_real_man = True)} is the number")