'''4. Shape Class with Subclasses for Different Shapes

Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
'''
# class Shape:

#     def area(self):
#         pass

#     def perimeter(self):
#         pass


# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# class Square(Shape):

#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

#     def perimeter(self):
#         return 4 * self.side


# class Triangle(Shape):

#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3

#     def perimeter(self):
#         return self.side1 + self.side2 + self.side3


# c = Circle(5)
# s = Square(4)
# t = Triangle(3, 4, 5)

# print("Circle Area =", c.area())
# print("Circle Perimeter =", c.perimeter())

# print("Square Area =", s.area())
# print("Square Perimeter =", s.perimeter())

# print("Triangle Perimeter =", t.perimeter())

class Shape:
    pass
class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
class Square(Shape):

    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s

c = Circle(5)
s = Square(4)

print("Circle Area =", c.area())
print("Square Area =", s.area())