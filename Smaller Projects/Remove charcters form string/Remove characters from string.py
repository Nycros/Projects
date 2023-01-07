

text = "This is a test to remove multiple characters. Also special characters.!/()))$%&}][]]{"
clean_text = text.translate(str.maketrans('', '', "assdf/$"))
print(clean_text)

# If we import the string library, we can use the method .punctuation to remove all special characters

import string

text = "This is a test to remove multiple characters. Also special characters.!/()))$%&}][]]{"
clean_text = text.translate(str.maketrans('', '', string.punctuation))
print(clean_text)
