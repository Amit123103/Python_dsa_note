'''2. Find the Key with Maximum Value
Question

Find the key having the highest value.
'''

marks = {'A': 78, 'B': 95, 'C': 88}

max_key = max(marks, key=marks.get)

print(max_key)
print(marks[max_key])