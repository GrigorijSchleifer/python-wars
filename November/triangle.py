import array

def row_sum_odd_numbers(n):
    arr = []
    # number will be "appended" if odd
    number = 1
    # increase until n then stop
    become_n = 0
    while become_n != n:
        # try out list comprehension
        arr = [number if number % 2 == 1 else None for i in range(become_n)]
        number += 1
        become_n += 1
    print(arr)

row_sum_odd_numbers(10)