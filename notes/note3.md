with keyword:
The with statement is used for resource management in Python. It automatically handles setup and cleanup operations, such as opening and closing files, making code safer, cleaner, and easier to read.

Global Scope:
A variable declared outside all functions is called a global variable. It belongs to the global scope and can be accessed throughout the program. To modify it inside a function, the global keyword must be used.

A namespace is a container that stores variable names and their values.

Python mainly has:

Built-in Namespace
Global Namespace
Local Namespace

LEGB Rule

Python searches for variables in this order:

L → Local Namespace
E → Enclosing Namespace
G → Global Namespace
B → Built-in Namespace


Global Namespace:
The global namespace is a dictionary-like structure that stores all names (variables, functions, classes, imported modules) defined at the top level of a Python program. It exists throughout the program's execution and can be accessed using the globals() function.