# virtual environment created with 
# python -m venv .venv
# venv is for python 3 and virtualenv is for python 2
import numpy as np

numbers = [13,10,5,2,9]

def product_array(numbers):
    prod_number = []
    for index in range(len(numbers)):
        prod_number.append(np.product(numbers[:index]) * np.product(numbers[index+1:]))
    return prod_number

product_array(numbers)