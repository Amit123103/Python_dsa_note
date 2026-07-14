'''4. Stone Piles Distribution

We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
'''


# Define a function named 'test' that takes an integer 'n' as input
def test(n):
    # Use a list comprehension to generate a list of values: n + 2 * i for i in the range from 0 to n-1
    return [n + 2 * i for i in range(n)]

# Assign a specific integer 'n' to the variable
n = 2

# Print the number of piles
print("Number of piles:", n)

# Print the header for the output
print("Number of stones in each pile:")

# Print the result of the test function applied to the integer 'n'
print(test(n))

# Assign a different integer 'n' to the variable
n = 10

# Print the number of piles
print("\nNumber of piles:", n)

# Print the header for the output
print("Number of stones in each pile:")

# Print the result of the test function applied to the modified integer 'n'
print(test(n))

# Assign another integer 'n' to the variable
n = 3

# Print the number of piles
print("\nNumber of piles:", n)

# Print the header for the output
print("Number of stones in each pile:")

# Print the result of the test function applied to the modified integer 'n'
print(test(n))

# Assign yet another integer 'n' to the variable
n = 17

# Print the number of piles
print("\nNumber of piles:", n)

# Print the header for the output
print("Number of stones in each pile:")

# Print the result of the test function applied to the modified integer 'n'
print(test(n))
