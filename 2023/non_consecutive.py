arr =[1,2,3,4,6,7,8]

def first_non_consecutive(arr: list) -> int:
    """
    Return first non-consecutive value from array
    Args: array of integers
    Return: Integer (first non-consecutive?
    """
    arr_test = []
    for ind in range(len(arr)):
        arr_test.append(arr[ind])
        print(f"Sum of arr_test: {arr_test} is {sum(arr_test)}")
        print(f"Sum of arr: {arr[:ind + 1]} is {sum(arr[:ind + 1])}")
        print("\n")
        # return arr_test[-1] if sum(arr_test) - sum(arr[:ind]) else None


first_non_consecutive(arr)
