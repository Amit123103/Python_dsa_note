'''8. Find Common Keys
Question

Find keys common in two dictionaries.
'''

d1 = {'a':1,'b':2,'c':3}
d2 = {'b':5,'c':6,'d':7}

common = []

for key in d1:
    if key in d2:
        common.append(key)

print(common)