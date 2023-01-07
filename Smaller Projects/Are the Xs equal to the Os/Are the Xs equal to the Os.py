string1 = "XoxxoxooxoxoxooxoOOXOXxOXoxOxOxOOOXoX"
string2 = "XXoo"
"""
Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False.
If the count of Xs and Os are equal, then the function should return True.
If the count isn't the same, it should return False. If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
"""

# Solution 1
def equal_x_o(string):
    num_x = string.upper().count('X')
    num_o = string.upper().count('O')

    if num_x == num_o:
        return True
    else:
        return False

print(equal_x_o(string1))


# Solution 2
def equal_x_o_2(string):
    count_x = 0
    count_o = 0

    for letter in string:
        if letter.lower() == 'x':
            count_x += 1
        elif letter.lower() == 'o':
            count_o += 1

    if count_x == count_o:
        return True
    else:
        return False

print(equal_x_o_2(string1))