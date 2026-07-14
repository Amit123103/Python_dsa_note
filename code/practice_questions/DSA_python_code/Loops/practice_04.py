''' Calculate the sum of all numbers from 1 to N
Practice Problem: Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
'''

# Take input from user and convert to integer
n = int(input("Enter number: "))

# Variable to store the sum
s = 0

# Loop from 1 to n (n+1 is used because range is exclusive)
for i in range(1, n + 1):
    s += i

print("Sum is:", s)