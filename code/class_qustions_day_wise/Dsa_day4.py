'''This is not overriding and not true overloading.

Python keeps only the latest definition of abc(), 
so the second function replaces the first one. 
Therefore abc(2,3) causes an error because Python only knows abc(a,b,c).'''
# def abc(a,b):
#     pass
# def abc(a, b,c):  #  function over riding  
#     pass
# abc(2,3)
# abc(2,3,4)

# from abc import ABC
# # Abstract class

# class classOne(ABC):
#     def display(self):
#         pass
# class ClassTwo(classOne):
#     def display(self):
#         print("This calss TWO")

# question 
#  class Student:
#      def student(self, name, marks, average):
#          self.name = name
#          self.marks = marks
#          self.average = average
         
         
# s1.Student("Alice",[85, 90, 78, 92, 88])
# print(s1.student)
# class Student:

#     def student(self, name, marks):
#         self.name = name
#         self.marks = marks 
    
#     def average(self):
#         return sum(self.marks) / len(self.marks)

# s1 = Student()
# s1.student("Alice", [85, 90, 78, 92, 88])

# print(s1.name)
# print(s1.marks)
# print(s1.average())

# 6 bank  account with deposit
# creat banckacount class with a balance atribute and two methoed  deposit(amount) that add funds to the balance and withdraw(amount) that deducts funds but prevents the balance from going below zero  
# starting balance of 1000, deposit 500, withdraw 200 then attempt to withdraw 2000.
''''''
# class BankAccount:
#     def __init__(self, initial_balance=0.0):
#         self.balance = float(initial_balance)

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Withdrawal failed: Insufficient funds!")
#         elif amount <= 0:
#             print("Withdrawal amount must be positive.")
#         else:
#             self.balance -= amount
#             print(f"Withdrew: ${amount:.2f}")

#     def get_balance(self):
#         print(f"Current Balance: ${self.balance:.2f}")
#         return self.balance

# my_account = BankAccount(50.0)    # Starts with $50
# my_account.get_balance()         # Current Balance: $50.00

# my_account.deposit(500.0)         # Deposited: $20.00
# my_account.withdraw(200.0)        # Withdrew: $40.00

# my_account.withdraw(2000.0)        # Withdrawal failed: Insufficient funds!
# my_account.get_balance()         # Current Balance: $30.00

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")
#         print(f"Current Balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")
#             print(f"Current Balance: {self.balance}")
#         else:
#             print("Not avalible balance")
#             print(f"Current Balance: {self.balance}")

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)
# account.withdraw(2000)
#  deposit = input("Enter Deposit amount: ")

#17. full time vs part time employee pay logic
# define Employee base class then create FullTimeEmployee and partimeEmployee subclass each implementing pay calculation logic
# input FulltimeEmployee("Alice", 60000) and partTimeEmployee("Bob", 500, 20)
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def calculate_pay(self):
#         pass


# class FullTimeEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary

#     def calculate_pay(self):
#         return self.salary


# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_pay(self):
#         return self.hourly_rate * self.hours_worked


# # Creating objects
# emp1 = FullTimeEmployee("Alice", 60000)
# emp2 = PartTimeEmployee("Bob", 500, 20)

# # Display pay
# print("Employee:", emp1.name)
# print("Pay:", emp1.calculate_pay())

# print("\nEmployee:", emp2.name)
# print("Pay:", emp2.calculate_pay())
#---------------------2nd answer--------------------------------#
# Inheritance using to solving this problem 
# class Employee:                  # parent class
#     def __init__(self, name):
#         self.name = name


# class FullTimeEmployee(Employee):   # child calss 
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary

#     def calculate_pay(self):  # fulltime  employee salary calcualte  
#         return self.salary


# class PartTimeEmployee(Employee):       # child class 
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_pay(self):
#         return self.hourly_rate * self.hours_worked # calculated pay value and retun thoese value


# # here is objects 
# emp1 = FullTimeEmployee("Alice", 60000)
# emp2 = PartTimeEmployee("Bob", 500, 20)

# # Display details  of employee
# print("Name:", emp1.name)
# print("Salary:", emp1.calculate_pay())

# print()

# print("Name:", emp2.name)
# print("Salary:", emp2.calculate_pay())
#--------------------------------3rd answer---------------------#   
# class Employee:
#     def __init__(self, name):
#         self.name = name
# class FullTimeEmployee(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
#     def pay(self):
#         return self.salary
# class PartTimeEmployee(Employee):
#     def __init__(self, name, rate, hours):
#         super().__init__(name)
#         self.rate = rate
#         self.hours = hours
#     def pay(self):
#         return self.rate * self.hours
# e1 = FullTimeEmployee("Alice", 60000)
# e2 = PartTimeEmployee("Bob", 500, 20)

# print(e1.name, "Pay =", e1.pay())
# print(e2.name, "Pay =", e2.pay())



# Questions 24
# vector Addition Using add Overloading
# write  a python Program that create a vector class represting a 2D vector  and implement the __add__
# dunder method so that two vector objects can be added using the + operator

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#     def display(self):
#         print("(", self.x, ",", self.y, ")")
# v1 = Vector(2, 3)
# v2 = Vector(4, 1)
# v3 = v1 + v2
# v3.display()
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, obj):
        return Vector(self.x + obj.x,self.y + obj.y)
v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print("Vector: ",(v3.x, v3.y))

        
    
        
