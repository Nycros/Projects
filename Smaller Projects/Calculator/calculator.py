"""
Write a Python function that accepts three parameters. The first parameter is an integer.
The second is one of the following mathematical operators: +, -, /, or *.* The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
"""

def calculator(string):
    elements = string.split()

    first = float(elements[0])
    second = float(elements[2])

    def div(first, second):
        return first / second

    def mult(first, second):
        return first * second
    
    def add(first, second):
        return first + second
    
    def sub(first, second):
        return first - second

    mapping = {'+': add, '-': sub, '*': mult, '/': div}

    return mapping[elements[1]](first, second)

user_input = input("Please enter a number, a operation and a second number: ")

print(calculator(user_input))

