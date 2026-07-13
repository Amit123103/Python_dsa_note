'''5. Substring in String List Check

Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
'''

# Define a function named 'test' that takes a list of strings 'str1' as input
def test(str1):
    # Check if the second-to-last character of the last string in 'str1' is a proper substring of the last string
    # and if the second-to-last character is different from the last character
    return str1[len(str1) - 2] in str1[len(str1) - 1] and str1[len(str1) - 2] != str1[len(str1) - 1]

# Create a list of strings 'str11' with specific elements
str11 = ["a", "abb", "sfs", "oo", "de", "sfde"]

# Print the original list
print("Original list:")
print(str11)

# Print the result of the test function applied to the 'str11' list
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))

# Create a different list of strings 'str11' with specific elements
str11 = ["a", "abb", "sfs", "oo", "ee", "sfde"]

# Print the original list
print("\nOriginal list:")
print(str11)

# Print the result of the test function applied to the modified 'str11' list
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))

# Create another list of strings 'str11' with specific elements
str11 = ["a", "abb", "sad", "ooaa", "esdfe", "sfsdfde", "sfsd", "sfsdf", "qwrew"]

# Print the original list
print("\nOriginal list:")
print(str11)

# Print the result of the test function applied to the modified 'str11' list
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))

# Create one more list of strings 'str11' with specific elements
str11 = ["a", "abb", "sad", "ooaa", "esdfe", "sfsdfde", "sfsd", "sfsdf", "qwsfsdfrew"]

# Print the original list
print("\nOriginal list:")
print(str11)

# Print the result of the test function applied to the modified 'str11' list
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))
