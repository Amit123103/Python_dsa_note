'''9. Check Whether a Number is Prime

Write a Python function that takes a number as a parameter and checks whether the number is prime or not. Python exercise solutions

Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
'''# Define a function named 'test_prime' that checks if a number 'n' is a prime number
# def test_prime(n):
#     # Check if 'n' is equal to 1
#     if (n == 1):
#         # If 'n' is 1, return False (1 is not a prime number)
#         return False
#     # Check if 'n' is equal to 2
#     elif (n == 2):
#         # If 'n' is 2, return True (2 is a prime number)
#         return True
#     else:
#         # Iterate through numbers from 2 to (n-1) using 'x' as the iterator
#         for x in range(2, n):
#             # Check if 'n' is divisible by 'x' without any remainder
#             if (n % x == 0):
#                 # If 'n' is divisible by 'x', return False (not a prime number)
#                 return False
#         # If 'n' is not divisible by any number from 2 to (n-1), return True (prime number)
#         return True

# # Print the result of checking if 9 is a prime number by calling the 'test_prime' function
# print(test_prime(9))
num = int(input("Enter a Number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
