# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python


'''
Every line should have increasing length by one
Fill line with odd numbers until length is one longer than the line before
Insert this filled list on next location
'''

def triange_row_sum(n):
    list_with_lists = [[]] * 10 
    number = 1
    for n_n in range(1, n+1):
        for nest_ls in list_with_lists:
            if number % 2 != 0 and len(nest_ls) < n_n:
                nest_ls.append(number)
                number += 1
    print(list_with_lists)

triange_row_sum(10) 



