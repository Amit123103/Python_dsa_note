If you already created a database named **ecom**, follow these steps to create tables inside it.

## Step 1: Open MySQL Workbench

* Open **MySQL Workbench**.
* Connect to your MySQL Server.

---

## Step 2: Select the Database

Run this command:

```sql
USE ecom;
```

This tells MySQL that all tables will be created inside the **ecom** database.

You can verify it:

```sql
SELECT DATABASE();
```

Output:

```
ecom
```

---

## Step 3: Create a Table

### Example 1: Customers Table

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50)
);
```

---

### Example 2: Products Table

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);
```

---

### Example 3: Orders Table

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);
```

---

### Example 4: Order Items Table

```sql
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);
```

---

## Step 4: View All Tables

```sql
SHOW TABLES;
```

Example output:

```
customers
products
orders
order_items
```

---

## Step 5: View Table Structure

```sql
DESCRIBE customers;
```

or

```sql
DESC customers;
```

---

## Step 6: See the SQL Used to Create a Table

```sql
SHOW CREATE TABLE customers;
```

---

## Step 7: Insert Sample Data

```sql
INSERT INTO customers(first_name, last_name, email, phone, city)
VALUES
('Amit', 'Kumar', 'amit@gmail.com', '9876543210', 'Delhi');
```

View the data:

```sql
SELECT * FROM customers;
```

---

# Complete E-commerce Database Structure

```
ecom
│
├── customers
│     ├── customer_id
│     ├── first_name
│     ├── last_name
│     ├── email
│     ├── phone
│     └── city
│
├── products
│     ├── product_id
│     ├── product_name
│     ├── category
│     ├── price
│     └── stock
│
├── orders
│     ├── order_id
│     ├── customer_id (FK)
│     ├── order_date
│     └── total_amount
│
└── order_items
      ├── order_item_id
      ├── order_id (FK)
      ├── product_id (FK)
      ├── quantity
      └── price
```

### Complete SQL Script

```sql
CREATE DATABASE ecom;

USE ecom;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

After running this script, your `ecom` database will contain four related tables suitable for a basic e-commerce application.
