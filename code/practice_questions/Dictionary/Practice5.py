'''5. Sort Dictionary by Value
Question

Sort a dictionary according to values.
'''

data = {'A':50,'B':20,'C':80,'D':40}

sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

print(sorted_dict)