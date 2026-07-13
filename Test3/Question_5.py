'''5. Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.'''


def adding_price(prices, newprice):
    index = 0
    while index < len(prices) and prices[index] < newprice:
        index += 1
    prices.insert(index, newprice)
    return prices


prices = [150, 220, 300, 450, 600]
newprice = int(input("Enter New Book Price: "))
print(adding_price(prices, newprice))