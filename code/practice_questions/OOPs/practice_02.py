'''2. Person Class with Age Calculation

Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
'''
from datetime import date 
class Calculation:
    def __init__(self, name, country, birth):
        self.name =name
        self.country = country
        self.birth = birth
    def display(self):
        current_year = date.today().year
        print("Age: " , current_year - self.birth)

person = Calculation("Amit", "India", 2005)


print(person.name)
print(person.country)
print(person.birth)
person.display()
    