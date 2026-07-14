'''3. Count Frequency of Elements
Question

Count the occurrence of each element in a list.
'''


numbers = [2,4,2,5,6,4,2]

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print(freq)