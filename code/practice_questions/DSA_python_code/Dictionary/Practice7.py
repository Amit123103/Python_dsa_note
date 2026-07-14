'''7. Group Words by First Letter
Question

Group words based on their first character.
'''

words = ["apple","ant","ball","bat","cat"]

group = {}

for word in words:
    first = word[0]
    group.setdefault(first, []).append(word)

print(group)