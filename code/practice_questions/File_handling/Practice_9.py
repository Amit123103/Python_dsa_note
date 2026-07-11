'''9. Find the shortest line'''
with open("data.txt", "r") as file:
    lines = file.readlines()

shortest = min(lines, key=len)

print(shortest)