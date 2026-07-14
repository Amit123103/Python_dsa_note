'''5. Count the number of characters'''


with open("data.txt", "r") as file:
    text = file.read()

print(len(text))