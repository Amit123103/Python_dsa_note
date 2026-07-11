'''4. Count the number of words'''

count = 0

with open("data.txt", "r") as file:
    for line in file:
        words = line.split()
        count += len(words)

print("Words:", count)