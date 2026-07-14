'''7. String Start Check Lambda

Write a Python program to find if a given string starts with a given character using Lambda.

Sample Output:
True
False
'''
# Define a lambda function 'starts_with' that checks if a given string starts with 'P'
starts_with = lambda x: True if x.startswith('P') else False

# Check if the string 'Python' starts with 'P' using the 'starts_with' lambda function
# Print the result which will be 'True' if the string starts with 'P', otherwise 'False'
print(starts_with('Python'))

# Redefine the lambda function 'starts_with' (same as before) to check if a string starts with 'P'
# Check if the string 'Java' starts with 'P' using the 'starts_with' lambda function
# Print the result which will be 'True' if the string starts with 'P', otherwise 'False'
print(starts_with('Java')) 

# str = lambda x : True if x.startswith('P') else False

# print(str("Python"))
# print(str("Lambda"))
