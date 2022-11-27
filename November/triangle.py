# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

arr_outer = []
arr_inner = []

'''
Every line should have increasing length by one
Fill line with odd numbers until length is one longer than the line before
Insert this filled list on next location
'''

number = 0

for i in range(10):
    print(f'i is {i}')
    number += 1
    print(f'number is {number}')
    if number % 2 > 0:
        print(f'number is {number}')
        arr_inner.append(number) 
        print(f'arr_inner is {arr_inner} and its length is {len(arr_inner)}')
        if len(arr_inner) == i:
            arr_outer.insert(i, arr_inner)
            arr_inner = []
            print(f'arr_outer is {arr_outer}')
    

print(arr_outer)

def triange_row_sum(n):
    list_with_lists = [[]] * n
    print(list_with_lists)
    for idx, nr in enumerate(list_with_lists):
        print(list_with_lists[idx]) 

triange_row_sum(10)

