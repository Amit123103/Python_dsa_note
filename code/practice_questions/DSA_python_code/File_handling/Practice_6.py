'''6. Copy one file to another'''

with open("data.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)