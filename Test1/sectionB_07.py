'''7. Create student.txt, write your name, then read and display it.'''
# file = open("student.txt", "w")
# file.write("Python test question")
# file.close()
# file = open("student.txt", "r")
# print(file.read())
# file.close()


def file_operation():
    file = open("student.txt", "w")
    file.write("Amit")
    file.close()
    file = open("student.txt", "r")
    print(file.read())
    file.close()
file_operation()