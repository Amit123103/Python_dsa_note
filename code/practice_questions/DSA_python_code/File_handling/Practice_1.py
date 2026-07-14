'''1. Read an entire file
Question

Read all the contents of a file.
'''

with open("data.txt", "r") as file:
    content = file.read()

print(content)