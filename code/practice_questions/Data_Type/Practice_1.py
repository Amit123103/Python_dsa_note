'''1. Calculate string length.

Write a Python program to calculate the length of a string.
'''


# Define a function named string_length that takes one argument, str1.
def string_length(str1):
    # Initialize a variable called count to 0 to keep track of the string's length.
    count = 0

    # Iterate through each character in the input string str1.
    for char in str1:
        # For each character encountered, increment the count by 1.
        count += 1

    # Return the final count, which represents the length of the input string.
    return count

# Call the string_length function with the argument 'w3resource.com' and print the result.
print(string_length('w3resource.com')) 
