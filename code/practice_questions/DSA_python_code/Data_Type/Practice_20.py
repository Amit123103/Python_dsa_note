''' Iterate Over Elements as Many Times as Its Count

Write a Python program that iterates over elements as many times as its count.

Sample Output: ['p', 'p', 'p', 'p', 'q', 'q']'''

# Import the Counter class from the collections module
from collections import Counter

# Create a Counter object 'c' with specified initial counts for keys 'p', 'q', 'r', and 's'
c = Counter(p=4, q=2, r=0, s=-2)

# Print the elements in the Counter 'c' as a list
print(list(c.elements())) 
