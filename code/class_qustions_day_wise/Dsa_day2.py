'''
data types:
- numeric
- sequence
- mapping
- set
- Boolean
'''
str ="1"
'''
operators:
    - arithmetic : + - * / % ** //
    - assignment : = += -= *= /= %= **= //=  
    - comparison : == != < > <= >=
    - logical : and or not
    - bitwise : & | ^ ~ << >>
    - identity : is is not
    - membership : in not in
    '''
'''
Control flow statements:
    conditional : if else
    - loop : for while
    - 

'''
# a = 10 # when we assign a value to a variable, python automatically assigns the data type to that variable.
# b= a
# c = 10
# print (a is c) # True
# for i in range(10):
#     print(i)
# counter = 0
# while counter < 10:
#     # print(counter)
#     counter += 1

'''
1. Divisible by 7 and Multiples of 5

Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

a = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        a.append(i)
    print(a)
    '''
'''
2. Temperature Converter

Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius 

temp = input("Enter the temperature: ")
unit = input("Enter the unit C and F: ")
for i in temp:
    if unit == "C":
        f = (9 * float(temp)/5) + 32
        print(f"{temp}C is {f} in Fahrenheit")
    elif unit == "F":
        c= (5 * (float(temp) -32))/9
        print(f"{temp}F is {c} in Celsius")
    else:
        print("Invalid unit")
'''
'''
3. Number Guessing Game

Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

num = 6
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == num:
        print("good guess")
        break
    else:
        print("try again")
    
'''
'''4. Construct Pattern (Diamond Pattern)

Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

abc = 5
for i in range(1, abc +1):
    for j in range(1, i +1):
        print("*", end = " ")
    print()
for i  in range(abc -1, 0, -1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()


# for i in range(1, 6):
#     print('* ' * i)
# for i in range(4, 0, -1):
#     print('* ' * i)
'''
'''
5. Reverse a Word

Write a Python program that accepts a word from the user and reverses it.

reverse_word = input("Enter a word: ")
print("the reverse of the word is: ", reverse_word[::-1])
'''
''' 6. Count Even and Odd Numbers

Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 5
Number of odd numbers : 4
num = input("Enter the number of elements in the series: ")
even_count = 0
odd_count = 0
for n in num:
    n = int(n)
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
'''
'''
7. Print Items with Types

Write a Python program that prints each item and its corresponding type from the following list.

Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print(f"{item} is of type {type(item)}")
'''
'''
8. Print Numbers 0 to 6 Except 3 and 6

Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.Scripting Languages

Note : Use 'continue' statement.

Expected Output : 0 1 2 4 5
num = 0
while num < 7:
     num += 1
     if num == 3 or num == 6:
         continue
print(num, end = " ")
'''
'''9. Fibonacci Series Between 0 and 50

Write a Python program to get the Fibonacci series between 0 and 50.

Note : The Fibonacci Sequence is the series of numbers :

Discover more
Programming Language
Data Management
Software
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34

data = []
a, b = 0, 1
while b < 50:
    data.append(b)
    a, b = b, a+b
print("Fibonacci series between 0 and 50:", data)
'''

# ---->>>>>>>Funtion questions----->>>>>>>>>>
'''1. Maximum of Three Numbers

Write a Python function to find the maximum of three numbers.

def maximum_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
print(maximum_of_three(10, 40, 30))
'''
'''2. Sum All Numbers in a List

Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)
Expected Output : 20

sum_list = [8, 2, 3, 0, 7]
def sum_of_list(list):
    total = 0
    for num in list:
        total += num
    return total
print("Sum of all numbers in the list:", sum_of_list(sum_list))
'''
'''3. Multiply All Numbers in a List

Write a Python function to multiply all the numbers in a list.

Sample List : (8, 2, 3, -1, 7)
Expected Output : -336

def mul_list(list):
    total = 1
    for num in list:
        total *= num
    return total
mul_list1 = [8, 2, 3, -1, 7]
print("Multipliocation of all numbers in the list: ", mul_list(mul_list1))
'''
'''4. Reverse a String

Write a Python program to reverse a string.

Sample String : "1234abcd"
Expected Output : "dcba4321"

str = "1234abcd"
print("the reverse of the string is: ", str[:: -1])
'''
'''
5. Factorial of a Number

Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a non-negative intweger to calculate its factorial: "))
print(factorial(n))
'''
# ------->>>>>>> file handaling ------>>>>>>>>>>>
# file_obj = open("file_name.txt",'d')
# # #file_obj.write(". something")
# # print(file_obj.readline())
# # print(file_obj.readline())
# file_obj.close()

# a = 4

# try:
#     print(a / 0)
# except:
#     print("Cannot divide by zero")

