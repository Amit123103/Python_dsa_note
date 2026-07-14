'''Print elements from a list present at odd index positions
Practice Problem: Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).
'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# range(start, stop, step)
for i in range(1, len(my_list), 2):
    print(my_list[i], end=" ")