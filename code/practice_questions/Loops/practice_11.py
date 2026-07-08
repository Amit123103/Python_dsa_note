'''Reverse a string using a for loop (no slicing)
Practice Problem: Write a program that takes a string and reverses it using a for loop. While Python’s [::-1] shortcut is famous, reversing a string manually is a classic way to understand how sequences are constructed.
'''

original_str = "Python"
reversed_str = ""

for char in original_str:
    # Prepending: Put the new character before the existing ones
    reversed_str = char + reversed_str

print(f"Original: {original_str}")
print(f"Reversed: {reversed_str}")