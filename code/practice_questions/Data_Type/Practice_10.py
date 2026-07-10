'''Add Key to Dictionary

Write a Python script to add a key to a dictionary. Scripting Languages

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''

# Create a dictionary 'd' with two key-value pairs.
d = {0: 10, 1: 20}

# Print the original dictionary 'd'.
print(d)

# Update the dictionary 'd' by adding a new key-value pair {2: 30}.
d.update({2: 30})

# Print the dictionary 'd' after the update, which now includes the new key-value pair.
print(d) 
