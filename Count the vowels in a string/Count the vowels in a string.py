"""
Create a function in Python that accepts a single word and returns the number of vowels in that word.
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""

def count_vowels(word):
    count = 0
    vowels = "aeiou"

    for vowel in vowels:
        count += word.lower().count(vowel)
    
    return count



word = input("Please enter a word: ")

print(count_vowels(word))