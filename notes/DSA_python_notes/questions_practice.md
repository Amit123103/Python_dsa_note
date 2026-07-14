These are excellent **intermediate-level Python practice questions**. Below are complete solutions with simple explanations.

---

# 1. Calculator Function

### Code

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid Choice")
```

---

# 2. Even or Odd

### Code

```python
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))
print(is_even(number))
```

---

# 3. Factorial Using Function

### Code

```python
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


number = int(input("Enter a number: "))
print("Factorial =", factorial(number))
```

---

# 4. Student Grade Function

### Code

```python
def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    else:
        return "Fail"


marks = int(input("Enter marks: "))
print("Grade:", calculate_grade(marks))
```

---

# 5. Student Class

### Code

```python
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)


s1 = Student("Amit", 20, "Python")
s2 = Student("Rahul", 21, "Java")

s1.display()
print()

s2.display()
```

---

# 6. Bank Account

### Code

```python
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance =", self.balance)


obj = BankAccount("Amit", 5000)

obj.deposit(2000)
obj.withdraw(1000)
obj.show_balance()
```

---

# 7. Rectangle Class

### Code

```python
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Area =", r.area())
print("Perimeter =", r.perimeter())
```

---

# 8. Employee Salary

### Code

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self, percent):

        increase = self.salary * percent / 100
        self.salary += increase

        print("Updated Salary =", self.salary)


e = Employee("Amit", 40000)

e.increment(10)
```

---

# 9. Inheritance Practice

### Code

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Bark")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()
```

---

# 10. Create and Write File

### Code

```python
file = open("students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()

print("Data Saved Successfully")
```

---

# 11. Read File

### Code

```python
file = open("students.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

---

# 12. Count Lines and Words

### Code

```python
file = open("students.txt", "r")

lines = file.readlines()

line_count = len(lines)

word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

file.close()

print("Lines =", line_count)
print("Words =", word_count)
```

---

# 13. Safe Division

### Code

```python
try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Answer =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 14. Number Validation

### Code

```python
try:

    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a number.")
```

---

# 15. File Not Found

### Code

```python
filename = input("Enter file name: ")

try:

    file = open(filename, "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("File not found.")
```

---

# Concepts Covered

| Question | Topic                                              |
| -------- | -------------------------------------------------- |
| 1        | Functions, Parameters, Return Values               |
| 2        | Functions, if-else, Return                         |
| 3        | Functions, Loops                                   |
| 4        | Functions, if-elif Ladder                          |
| 5        | Class, Object, Constructor, Methods                |
| 6        | Objects, Instance Variables, Methods               |
| 7        | Class, Methods, Formula Implementation             |
| 8        | Object Manipulation, Updating Instance Variables   |
| 9        | Inheritance, Method Overriding                     |
| 10       | File Creation, `write()`, `close()`                |
| 11       | File Reading, Looping Through a File               |
| 12       | `readlines()`, `split()`, Counting Lines and Words |
| 13       | `try`, `except`, `ZeroDivisionError`               |
| 14       | `try`, `except`, `ValueError`                      |
| 15       | `FileNotFoundError`, File Handling                 |

These 15 programs cover the core Python concepts that are commonly asked in interviews, college practical exams, and coding assessments.
