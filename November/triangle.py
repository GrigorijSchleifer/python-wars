import numpy as np

def row_sum_odd_numbers(n):
    number = 0
    len_arr = 1
    arr_outer = []
    arr_inner = []
    for arr in arr_outer:
        number += 1
        if number % 2 == 1:
            arr_outer.append(arr_inner.extend(number))
            len_arr += 1 
    print(arr_outer)

row_sum_odd_numbers(10)

number = 0
len_arr = 1
arr_outer = []
arr_inner = []
for i in range(10):
    number += 1
    if number % 2 != 1 and i < 10:
        arr_outer.append(arr_inner.extend(number))
        len_arr += 1 
    print(arr_outer)

for i in range(10):
    arr_inner.extend(i)
    print(i)