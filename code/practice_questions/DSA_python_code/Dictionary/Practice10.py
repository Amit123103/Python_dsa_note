'''10. Nested Dictionary Traversal
Question

Print every student's subject marks.'''


students = {
    "A": {"Math":90, "Science":80},
    "B": {"Math":75, "Science":85}
}

for student, subjects in students.items():
    print(student)
    for subject, marks in subjects.items():
        print(subject, marks)