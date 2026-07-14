'''2. Read a file line by line'''

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())