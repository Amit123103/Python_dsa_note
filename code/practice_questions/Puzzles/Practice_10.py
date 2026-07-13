'''10. Split Matched Parentheses Groups

Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
'''

# License: https://bit.ly/3oLErEI

# Define a function named 'test' that takes a string 'combined' as input
def test(combined):
    # Initialize an empty list 'ls' to store separate parentheses groups
    ls = []
    
    # Initialize an empty string 's2' to build individual parentheses groups
    s2 = ""
    
    # Iterate through each character in the modified 'combined' string (spaces removed)
    for s in combined.replace(' ', ''):
        # Concatenate the character to 's2'
        s2 += s
        
        # Check if the count of opening parentheses '(' equals the count of closing parentheses ')'
        if s2.count("(") == s2.count(")"):
            # Append the built parentheses group to the 'ls' list
            ls.append(s2)
            
            # Reset 's2' to an empty string for the next parentheses group
            s2 = ""
    
    # Return the list of separate parentheses groups
    return ls

# Assign a specific string 'combined' to the variable
combined = '( ()) ((()()())) (()) ()'

# Print the original parentheses string
print("Parentheses string:")
print(combined)

# Print a message indicating the operation to be performed on the string
print("Separate parentheses groups of the said string:")

# Print the result of the test function applied to the 'combined' string
print(test(combined))

# Assign a different string 'combined' to the variable
combined = '() (( ( )() (  )) ) ( ())'

# Print the original parentheses string
print("\nParentheses string:")
print(combined)

# Print a message indicating the operation to be performed on the string
print("Separate parentheses groups of the said string:")

# Print the result of the test function applied to the modified 'combined' string
print(test(combined))
