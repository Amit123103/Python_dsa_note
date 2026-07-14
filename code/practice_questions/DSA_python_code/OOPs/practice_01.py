'''1. Circle Class for Area and Perimeter

Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
'''
'''
User Input
    │
    ▼
Circle Object Created
    │
    ▼
Stores Radius
    │
    ├──► area()
    │        │
    │        ▼
    │   Calculate Area
    │
    └──► perimeter()
             │
             ▼
      Calculate Perimeter
             │
             ▼
          Print Result
          '''
'''
# Import the math module to access mathematical functions like pi
import math

# Define a class called Circle to represent a circle
class Circle:
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius
    
    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_circle_area(self):
        return math.pi * self.radius**2
    
    # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
# Prompt the user to input the radius of the circle and convert it to a floating-point number
radius = float(input("Input the radius of the circle: "))

# Create a Circle object with the provided radius
circle = Circle(radius)

# Calculate the area of the circle using the calculate_circle_area method
area = circle.calculate_circle_area()

# Calculate the perimeter of the circle using the calculate_circle_perimeter method
perimeter = circle.calculate_circle_perimeter()

# Display the calculated area and perimeter of the circle
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter) 

'''

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area =", 3.14 * self.radius * self.radius)

    def perimeter(self):
        print("Perimeter =", 2 * 3.14 * self.radius)


r = float(input("Enter Radius: "))

c = Circle(r)

c.area()
c.perimeter()
