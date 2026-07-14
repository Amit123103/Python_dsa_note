'''15. Password Validity Checker

Write a Python program to check the validity of passwords input by users.

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''

pass = input("Enter Your password: ")
# if len(pass) >= 6 and len(pass) <= 16 and 
# any

l = 0
d = 0
u = 0
s = 0
for ch in pass:
    if ch >= 'a' and ch 'z'
     