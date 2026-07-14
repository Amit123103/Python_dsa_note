'''17. Create a Chain of Function Decorators (Bold, Italic, Underline, etc.)

Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
'''
# def bold(func):
#     def wrapper():
#         return "<b>" + func() + "</b>"
#     return wrapper


# def italic(func):
#     def wrapper():
#         return "<i>" + func() + "</i>"
#     return wrapper


# def underline(func):
#     def wrapper():
#         return "<u>" + func() + "</u>"
#     return wrapper


# @bold
# @italic
# @underline
# def message():
#     return "Hello World"


# print(message())
# Define a decorator 'make_bold' that adds bold HTML tags to the wrapped function's return value
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

# Define a decorator 'make_italic' that adds italic HTML tags to the wrapped function's return value
def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

# Define a decorator 'make_underline' that adds underline HTML tags to the wrapped function's return value
def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

# Apply multiple decorators (@make_bold, @make_italic, @make_underline) to the 'hello' function
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"

# Print the result of the decorated 'hello' function, which adds HTML tags for bold, italic, and underline

print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
