'''16. Create and Print a List of Squares for Numbers 1 to 30

Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
'''
# def values():
#     l = list()
#     for i in range(1, 30):
#         l.append(i**2)
#     print(l)
# values()
# Define a function named 'printValues' that generates a list of squares of numbers from 1 to 20
def printValues():
    # Create an empty list 'l'
    l = list()
    
    # Iterate through numbers from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Calculate the square of 'i' and append it to the list 'l'
        l.append(i**2)
    
    # Print the list containing squares of numbers from 1 to 20
    print(l)

# Call the 'printValues' function to generate and print the list of squares
printValues() 
