def min_value(arr: list) -> int:
    min_value = arr[0] 
    for val in arr:
        if val < min_value: 
            min_value = val
    return min_value 


min_value([78, 56, 232, 12, 11, 43])