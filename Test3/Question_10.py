'''10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found.
''' 

marks = [
    55, 78, 92, 45, 88, 67, 82, 90, 75, 60,
    58, 72, 95, 48, 85, 70, 79, 91, 84, 62,
    52, 74, 98, 42, 80, 68, 77, 89, 83, 65,
    50, 76, 99, 44, 87, 69, 73, 86, 81, 63,
    54, 71, 96, 46, 84, 61, 74, 94, 86, 64
]

def selection_sort(marks):
    n = len(marks)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if marks[j] < marks[min_index]:
                min_index = j
        marks[i], marks[min_index] = marks[min_index], marks[i]
    return marks

def linear_search(marks, school_mark):
    for i in range(len(marks)):
        if marks[i] == school_mark:
            return i
    return -1

sorted_marks = selection_sort(marks)
print("Sorted Marks: ",sorted_marks)
report = int(input("Enter Mark: "))

user_marks = linear_search(sorted_marks, report)

if user_marks != -1:
    print("Mark Found at Position:", user_marks)
else:
    print("Mark Not Found")