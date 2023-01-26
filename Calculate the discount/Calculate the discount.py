"""
Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer.
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied.
For example, if the price is 100 and the discount is 20, the function should return 80.
"""

# Function Definition:

# Signature: Calcualte the discount price of an item.
#   orig_price, discount --> discount_price         # List all the inputs to the function on the left side. If 5 Variables are needed, then list all 5 also applies to the output.
# Purpose:
#   Takes the original price and the discount in percent and calculate the discount price.
# Examples, Tests, make sure to cover all edge cases:
#   calc_discount(17.23, 10) --> 15.51
#   calc_discount(27, 50) --> 13.50
#   calc_discount(-10, 50) --> -5.0
#   calc_discount("Hallo", 50) --> Please enter a valid price.
#   calc_discount(74, 150) --> Please enter a valid discount
# Template:
#   def discount(orig_price, discount):
#        ... orig_price --> float
#        ... XX --> float percentage
#        ... return discount price --> float
# Function:

def calc_discount(orig_price, discount):
    
    try:
        float(orig_price)
    except:
        return "Please enter a valid price."

    try:
        float(discount)
    except:
        return "Please enter a valid discount"

    if float(discount) > 100 or float(discount) < 0:
        return "Please enter a valid discount"

    return round((float(orig_price)* (1- (float(discount)/ 100))), 2)
# ==================================

orig_price = 17.23
discount = 10
print(calc_discount(orig_price, discount))

orig_price = 27
discount = 50
print(calc_discount(orig_price, discount))

orig_price = -10
discount = 50
print(calc_discount(orig_price, discount))

orig_price = "Hallo"
discount = 50
print(calc_discount(orig_price, discount))

orig_price = 74
discount = 150
print(calc_discount(orig_price, discount))

orig_price = 0
discount = 25
print(calc_discount(orig_price, discount))

orig_price = 30
discount = -25
print(calc_discount(orig_price, discount))