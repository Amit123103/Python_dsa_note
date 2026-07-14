'''15. Sort Hyphen-Separated Sequence of Words Alphabetically

Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Python module tutorials

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''
# text = input("Enter words: ")

# result = '-'.join(sorted(text.split('-')))

# print(result)

def sort_words(sequence):
    words = sequence.split('-')
    words.sort()
    result = '-'.join(words)
    return result

text = "green-red-yellow-black-white"
print(sort_words(text))