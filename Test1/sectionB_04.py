'''4. Print the multiplication table of a given number up to 10.'''
# n = int(input("Enter number: "))
# for i in range(1, 11):
#     print(n, "X", i, ":", n * i)

    
def table():
    n = int(input("Enter number: "))
    for i in range(1, 11):
        print(n, "X", i, ":", n * i)
table()