'''Display numbers from a list using a loop
Practice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions:

The number must be divisible by five.
If the number is greater than 150, skip it and move to the next.
If the number is greater than 500, stop the loop entirely.
'''
numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    # Condition 3: Stop the loop if number > 500
    if item > 500:
        break
    
    # Condition 2: Skip the number if > 150
    if item > 150:
        continue
    
    # Condition 1: Print if divisible by 5
    if item % 5 == 0:
        print(item)