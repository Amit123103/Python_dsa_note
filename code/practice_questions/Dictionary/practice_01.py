'''1. Merge Two Dictionaries
Question

Merge two dictionaries. If a key exists in both, add their values.
'''


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

result = dict1.copy()

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

print(result)