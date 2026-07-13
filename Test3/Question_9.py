'''9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.'''

books = [1030, 1120, 3145, 6160, 7180, 210, 5250, 3000]
def binary_search(books, low, high, book_id):
    if low > high:
        return -1
    mid_value = (low + high) // 2
    if books[mid_value] == book_id:
        return mid_value
    elif book_id < books[mid_value]:
        return binary_search(books, low, mid_value- 1, book_id)
    else:
        return binary_search(books, mid_value + 1, high, book_id)



book_id = int(input("Enter Book ID: "))
searchbook = binary_search(books, 0, len(books) - 1, book_id)
if searchbook != -1:
    print("Book Found at Index:", searchbook)
else:
    print("Book Not Found")