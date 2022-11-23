import numpy as np

def row_sum_odd_numbers(n):
    number = 0
    len_arr = 1
    arr_outer = []
    arr_inner = []
    for arr in arr_outer:
        number += 1
        if number % 2 == 1 and len(arr) < len_arr:
            arr_outer.append(arr_inner.append(number))
            len_arr += 1 
    print(arr_outer)

row_sum_odd_numbers(10)

arr1 = [1, 2, 3] 
arr2 = [4, 5, 6] 
arr3 = (arr2)
print(arr3)

for i in range(10):
    number = 0
    len_arr = 1
    arr_outer = []
    arr_inner = []
    
    if i % 2 == 1:
        arr_outer.append(arr_inner.append(number))
        print(i)
