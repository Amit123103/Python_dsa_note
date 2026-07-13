'''2. Product ID Search
An e-commerce website stores product IDs in ascending order.
Write a program to find whether a customer-entered product ID exists in
the inventory. If it exists, display its index; otherwise, display "Product
Not Available."'''

product_ids = [102, 105, 112, 220, 432, 521, 845, 918]

search_id = int(input("Enter Product ID: "))

if search_id in product_ids:
    print("Product Found at Index:", product_ids.index(search_id))
else:
    print("Product Not Available")