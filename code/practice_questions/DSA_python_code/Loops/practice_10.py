'''Print list in reverse order using a loop
Practice Problem: Given a list, iterate it in reverse order and print each element.
'''


# list1 = [10, 20, 30, 40, 50]

# # Use the reversed() function for clean iteration
# for item in reversed(list1):
#     print(item)

list1 = [10, 20, 30, 40, 50]
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])