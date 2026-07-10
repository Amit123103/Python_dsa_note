'''2. Count character frequency in a string.

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''


# Define a function named char_frequency that takes one argument, str1.
def char_frequency(str1):
    # Initialize an empty dictionary named 'dict' to store character frequencies.
    dict = {}
    
    # Iterate through each character 'n' in the input string str1.
    for n in str1:
        # Retrieve the keys (unique characters) in the 'dict' dictionary.
        keys = dict.keys()
        
        # Check if the character 'n' is already a key in the dictionary.
        if n in keys:
            # If 'n' is already a key, increment its value (frequency) by 1.
            dict[n] += 1
        else:
            # If 'n' is not a key, add it to the dictionary with a frequency of 1.
            dict[n] = 1
    
    # Return the dictionary containing the frequency of each character in the input string.
    return dict

# Call the char_frequency function with the argument 'google.com' and print the result.
print(char_frequency('google.com')) 
