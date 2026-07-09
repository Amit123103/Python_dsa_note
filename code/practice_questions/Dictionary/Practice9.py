'''9. Sum All Dictionary Values
Question

Find the total of all values.

'''


marks = {'Math':80,'Science':90,'English':85}

total = 0

for value in marks.values():
    total += value

print(total)