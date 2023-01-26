"""
Create a function in Python that accepts two parameters.
The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.
If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.
"""

# Function Definition:
numbers_1 = []
order_1 = "asc"
numbers_2 = [1, 2, 3, 4, 5, 6]
order_2 = "desc"
numbers_3 = [4, 3, 2, 1]
order_3 = "asc"
numbers_4 = [3, 7, 3, 2, 1]
order_4 = "none"
numbers_5 = [3, 7, 3, 2, 'f']
order_5 = "desc"

# Signature:
#   list, string --> list         # List all the inputs to the function on the left side. If 5 Variables are needed, then list all 5 also applies to the output.
# Purpose:
#   takes a list and a string and sorts the list in order, that in the string is given.
# Examples, Tests, make sure to cover all edge cases:
#   sort_list(numbers_1, order_1) --> []
#   sort_list(numbers_2, order_2) --> [6, 5, 4, 3, 2, 1]
#   sort_list(numbers_3, order_3) --> [1, 2, 3, 4]
#   sort_list(numbers_4, order_4) --> [3, 7, 3, 2, 1]
#   sort_list(numbers_5, order_5) --> "Please enter a valid list with only numbers"
# Template:
#   def sort_list(numbers, order):
#        ... number_1 --> lsit
#        ... order_1 --> string
#        ... return ans --> list
# Function:

def sort_list(numbers, order):
    
    if not all(isinstance(x, int) for x in numbers):
        return "Please enter a valid list with only numbers"

    if not all(type(x) == int for x in numbers):
        return "Please enter a valid list with only numbers"

    if order == "asc":
        numbers.sort(reverse = False)
    elif order == "desc":
        numbers.sort(reverse = False)
    else:
        numbers
    
    return numbers

# ==================================

print(sort_list(numbers_1, order_1))
print(sort_list(numbers_2, order_2))
print(sort_list(numbers_3, order_3))
print(sort_list(numbers_4, order_4))
print(sort_list(numbers_5, order_5))