'''6. Invert a Dictionary
Question

Swap keys and values.
'''

student = {'A':101,'B':102,'C':103}

inverse = {}

for key, value in student.items():
    inverse[value] = key

print(inverse)