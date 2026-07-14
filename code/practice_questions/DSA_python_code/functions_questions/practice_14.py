'''14. Check if a String is a Pangram

Write a Python function to check whether a string is a pangram or not. Data structures course

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''
# def is_pangram(s):
#     letters = set()

#     for ch in s.lower():
#         if ch.isalpha():
#             letters.add(ch)

#     return len(letters) == 26


# text = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(text))

# Import the 'string' and 'sys' modules
import string
import sys

# Define a function named 'ispangram' that checks if a string is a pangram
def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set 'alphaset' containing all lowercase letters from the provided alphabet
    alphaset = set(alphabet)
    
    # Convert the input string to lowercase and create a set from it
    str_set = set(str1.lower())
    
    # Check if the set of lowercase characters in the input string covers all characters in 'alphaset'
    return alphaset <= str_set

# Print the result of checking if the string is a pangram by calling the 'ispangram' function
print(ispangram('The quick brown fox jumps over the lazy dog')) 
