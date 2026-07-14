'''14. Count Digits and Letters in a String

Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits 2
'''

str_vl = input("Enter a string: ")

letters = 0
digits = 0

for char in str_vl:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        print("Invaild String")

print("Number of letters:", letters)
print("Number of digits:", digits)

# # while looop using to creating 

# str_vl = input("Enter a string: ")

# letters = 0
# digits = 0
# i = 0

# # for char in str_vl:
# while i < len(str_vl):    # len function provide us length of sequence
#     if str_vl[i].isalpha():
#         letters += 1
#     elif str_vl[i].isdigit():
#         digits += 1
# i += 1

# print("Number of letters:", letters)
# print("Number of digits:", digits)




# counter = 0
# Counter = len(str_vl)
# while Counter > 0:
#     print(str_vl[counter])
