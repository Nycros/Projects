"""
Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent "4444 4444 4444 4444", then it should return "4444".
"""

def hide(card_number):
    res = ''
    
    for index, digit in enumerate(card_number):
        if index > len(card_number) - 5:
            break
        
        if digit.isdigit():
            res += '*'
        else:
            res += digit
            
    res += card_number[-4:]

    return res


card_number = "4444 4444 4444 4444"
print(hide(card_number))

