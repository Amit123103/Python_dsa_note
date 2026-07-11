'''3. Count the number of lines in a file'''

count = 0

with open("data.txt", "r") as file:
    for line in file:
        count += 1

print("Total Lines:", count)