"""
Write a function in Python that accepts a decimal number and returns the equivalent binary number.
To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
https://www.rapidtables.com/convert/number/decimal-to-binary.html?x=56.23
"""

# We have a decimal number.
# we should convert that number into the binary form

# therefore, we need to split the number into whole number and fraction number.
# each of them i need to transform into a binary number.
# afterwards, i combine both of them again

# Data Definition:

# number is atomic/ integer
# interpretation:
#   a decimal number
# Examples, should show different states of the data:
#   n_1 --> 56.23
#   n_2 --> 12
# Template:
#   def dec_to_bin(number):
#       ... number
#       return string
# Template rule used: atomic non distinct
# ==================================

# Function Definition:

# Signature:
#   number --> string         # List all the inputs to the function on the left side. If 5 Variables are needed, then list all 5 also applies to the output.
# Purpose:
#   Takes a decial number and converts it into the binary representation
# Examples, Tests, make sure to cover all edge cases:
#   dec_to_bin(56.23) --> 111000.001110101110000101
#   dec_to_bin(12) --> 1100
# Template:
#   def dec_to_bin(number):
#        ... number
#        ... return string
# Function:

# def XXX(XX, YY):
#     ... A
# ==================================

def dec_to_bin(number):
    res = []
    dec_places = 18

    quotient = int(round(float(number) * (2 ** dec_places),0))

    while quotient > 1:
        # print(f"DEBUG: Quotient: {quotient}")
        remainder = quotient % 2
        quotient = quotient // 2
        res.append(str(remainder))
    
    res.append(str(1))
    res.insert(dec_places, '.')
    ans = ''.join(res[::-1])
    
    return ans


# number = input("Please enter a number to transform into binary: ")

number_1 = 56.23
number_2 = 12
number_3 = 173.253
print(f"The binary representation of the number {number_1} is: {dec_to_bin(number_1)}")
print(f"The binary representation of the number {number_2} is: {dec_to_bin(number_2)}")
print(f"The binary representation of the number {number_3} is: {dec_to_bin(number_3)}")