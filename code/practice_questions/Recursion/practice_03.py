'''Integer to String Conversion in Any Base Using Recursion

Write a Python program to convert an integer to a string in any base using recursion .
'''

# Define a function named to_string that converts a number 'n' to a string representation
# in a given 'base' using a character set "0123456789ABCDEF"
def to_string(n, base):
    # Define a character set for the conversion in hexadecimal format
    conver_tString = "0123456789ABCDEF"
    
    # Check if the number 'n' is less than the specified base
    if n < base:
        # If 'n' is less than the base, return the corresponding character from the character set
        return conver_tString[n]
    else:
        # If 'n' is greater than or equal to the base, recursively call the to_string function
        # to convert the quotient (n // base) to a string and concatenate it with the remainder
        # (n % base) represented in the character set
        return to_string(n // base, base) + conver_tString[n % base]

# Print the result of calling the to_string function with the input values 2835 and 16
print(to_string(2835, 16))

# def string(num, base):
#     convert_string = "012345667ABCD"
#     if num <base:
#         return convert_string[num]
#     else:
#         return string(num // base, base) + convert_string [num % base]
    
# print(string(2853, 16))