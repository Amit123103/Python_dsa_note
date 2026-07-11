'''10. Count vowels in a file'''

vowels = "aeiouAEIOU"
count = 0

with open("data.txt", "r") as file:
    text = file.read()

for ch in text:
    if ch in vowels:
        count += 1

print(count)