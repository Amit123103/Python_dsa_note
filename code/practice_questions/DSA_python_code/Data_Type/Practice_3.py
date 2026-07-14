'''3. Get string of first and last 2 chars.

Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''

# Define a function named string_both_ends that takes one argument, 'str'.
def string_both_ends(str):
    # Check if the length of the input string 'str' is less than 2 characters.
    if len(str) < 2:
        # If the string is shorter than 2 characters, return an empty string.
        return ''

    # If the string has at least 2 characters, concatenate the first two characters
    # and the last two characters of the input string and return the result.
    return str[0:2] + str[-2:]

# Call the string_both_ends function with different input strings and print the results.
print(string_both_ends('w3resource'))  # Output: 'w3ce'
print(string_both_ends('w3'))          # Output: 'w3w3'
print(string_both_ends('w'))           # Output: '' 
