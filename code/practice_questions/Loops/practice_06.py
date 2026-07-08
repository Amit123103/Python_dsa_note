'''Calculate the cube of all numbers from 1 to a given number
Practice Problem: Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1
'''

input_number = 6

for i in range(1, input_number + 1):
    # Calculate cube and print with formatting
    print(f"Current Number is : {i}  and the cube is {i ** 3}")