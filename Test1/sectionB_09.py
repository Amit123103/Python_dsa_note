'''9. Create a Student class with name and age, then display them.'''
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s = Student("Amit", 20)
# print("Name:", s.name)
# print("Age:", s.age)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def display_student():
    s = Student("Amit", 20)
    print("Name:", s.name)
    print("Age:", s.age)
display_student()