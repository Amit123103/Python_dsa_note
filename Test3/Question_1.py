'''. Student Roll Number Search
A teacher has stored the roll numbers of students in a list in the order
they registered. The list is not sorted.
Write a program to check whether a given roll number exists in the list.
If found, display its position; otherwise, print "Student Not Found."
'''

def search_roll(roll_list, roll_no):
    for index, roll in enumerate(roll_list, start=1):
        if roll == roll_no:
            return index
    return "Student Not Found"


roll_list = [105, 102, 110, 101, 108, 115, 120]

roll_no = int(input("Enter Roll Number: "))

print(search_roll(roll_list, roll_no))