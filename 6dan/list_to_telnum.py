# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
num_arr = [0,1,2,3,4,5,6,7,8,9] 

def create_phone_number(n):
    #your code here
    return print(f"({num_arr[0:3]}) {num_arr[3:5]}-{num_arr[6:9]}")

create_phone_number(num_arr)