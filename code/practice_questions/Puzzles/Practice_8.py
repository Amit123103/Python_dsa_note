'''8. Split String into Words and Separators

Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
'''



# Define a function named 'test' that takes a string 'string' as input
def test(string):
    # Import the 're' module for regular expressions
    import re
    
    # Use regular expression to split the string into words and separators and store in the 'merged' list
    merged = re.split(r"([ ,]+)", string)
    
    # Return a list containing two sublists: words (even indices) and separators (odd indices) from the 'merged' list
    return [merged[::2], merged[1::2]]

# Assign a specific string 's' to the variable
s = "W3resource Python, Exercises."

# Print the original string
print("Original string:", s)

# Print a message indicating the operation to be performed on the string
print("Split the said string into 2 lists: words and separators:")

# Print the result of the test function applied to the string 's'
print(test(s))

# Assign a different string 's' to the variable
s = "The dance, held in the school gym, ended at midnight."

# Print the original string
print("\nOriginal string:", s)

# Print a message indicating the operation to be performed on the string
print("Split the said string into 2 lists: words and separators:")

# Print the result of the test function applied to the modified string 's'
print(test(s))

# Assign another string 's' to the variable
s = "The colors in my studyroom are blue, green, and yellow."

# Print the original string
print("\nOriginal string:", s)

# Print a message indicating the operation to be performed on the string
print("Split the said string into 2 lists: words and separators:")

# Print the result of the test function applied to the modified string 's'
print(test(s))
