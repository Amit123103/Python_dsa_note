'''Group Anagrams Using a Dictionary
Problem

Given a list of strings, group all the anagrams together.

Two words are anagrams if they contain the same characters in a different order.
'''

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))