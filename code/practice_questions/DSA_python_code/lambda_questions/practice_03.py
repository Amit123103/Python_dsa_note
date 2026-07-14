'''3. Tuple Sorting Lambda

Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
# subjects = [
#     ('English', 88),
#     ('Science', 90),
#     ('Maths', 97),
#     ('Social sciences', 82)
# ]

# print("Original list:")
# print(subjects)

# subjects.sort(key=lambda x: x[1])

# print("\nSorted list:")
# print(subjects)

# Create a list of tuples named 'subject_marks', each tuple containing a subject and its corresponding marks
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Display the original list of tuples to the console
print("Original list of tuples:")
print(subject_marks)

# Sort the 'subject_marks' list of tuples based on the second element of each tuple (the marks),
# using a lambda function as the sorting key to extract the second element
subject_marks.sort(key=lambda x: x[1])

# Display the sorted list of tuples to the console
print("\nSorting the List of Tuples:")
print(subject_marks) 
