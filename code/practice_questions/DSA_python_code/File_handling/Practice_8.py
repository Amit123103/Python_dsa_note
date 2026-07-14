'''8. Find the longest line'''
with open("data.txt", "r") as file:
    longest = ""

    for line in file:
        if len(line) > len(longest):
            longest = line

print(longest)