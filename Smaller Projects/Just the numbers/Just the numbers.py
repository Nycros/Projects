"""
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings.
The function should return a list with only the integers in the original list in the same order.
"""

# Function Definition:

# Signature:
#   list --> list        # List all the inputs to the function on the left side. If 5 Variables are needed, then list all 5 also applies to the output.
# Purpose:
#   takes a list with integers and strings and returns the same list, but without all the strings.
# Examples, Tests, make sure to cover all edge cases:
#   clean(list_1) [1,'a', 2, 'b', 3, 'c', 4, 'd'] --> [1, 2, 3, 4]
#   clean(list_2) [1, "hello", 14, "234", "this", 8] --> [1, 14, 8]
# Template:
#   def clean(elements):
#        ... elements --> list[integer, string]
#        ... return res--> lsit[integers]
# Function:

def clean(elements):
    res = []

    for element in elements:
        if type(element) is int:
            res.append(element)

    return res
# ==================================

elements_1 = [1,'a', 2, 'b', 3, 'c', 4, 'd']
print(clean(elements_1))

elements_2 = [1, "hello", 14, "234", "this", 8]
print(clean(elements_2))