"""
Create a Python function that accepts a string.
The function should return a string, with each character in the original string doubled.
If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
"""

# Function Definition:

string_1 = "hallo"
string_2 = "123f!"
string_3 = ""
string_4 = 4

# Signature:
#   string --> string         # List all the inputs to the function on the left side. If 5 Variables are needed, then list all 5 also applies to the output.
# Purpose:
#   The function takes a string and returns a string, where each character is doubled.
# Examples, Tests, make sure to cover all edge cases:
#   double(string_1) --> "hhaalllloo"
#   double(string_2) --> "112233ff!!"
#   double(string_3) --> ""
#   double(string_4) --> "Please enter a valid string"
# Template:
#   def double(string):
#        ... string --> string
#        ... return ans --> string
# Function:

def double(string):
    ans = ""

    if type(string) is not str:
        return "Please enter a valid string"

    for char in string:
        ans += char * 2
    
    return ans
# ==================================

print(double(string_1))
print(double(string_2))
print(double(string_3))
print(double(string_4))