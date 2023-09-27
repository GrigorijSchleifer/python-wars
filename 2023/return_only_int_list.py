def filter_list(l):
    'return a new list with the strings filtered out'
    return [item for item in l if isinstance(item, int)]

lst = [1, 2, "aasf", "1", "123", 123]

only_integers = filter_list(lst)
print(only_integers)

