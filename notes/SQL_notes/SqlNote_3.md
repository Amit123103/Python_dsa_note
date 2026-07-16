IN c=when inserting data into table where we assigning the ID name nad  and in vaule we storing it and we can't chnges thoes values


key is medium where to identify  key is idefiy the uniquely identification
key we medium to create relationship

### what is primary key ?
primary kry is main key and where we identify the colums in tables which colums we have and what we have to chnges according to chnges that colum and dtails using primary key 

two properties of primary key
1. only store unique key
2. ondelete coscade -- when we delte row or first record in tabel then can't retrive an dand also not going to add gain 1 id if delte and going to start with 2 always


#### what is forien key

parent child property

in forien key is bi directional
when two tables connect with each other with need to cnnect with reference object with connecting with first table with that refercnce key connect with first table called forien key


### Types of JOIN

1. inner
2. outer
3. left
4. right
5. full
important join -- ### natural join, cross 


combining two tables in diffenre t  to join the table




Outer join where two metho d to joing first make relation to join and second isolated comman data and output it  and 1 one one more otimize but complicated



# 📘 SQL Notes – Primary Key, Foreign Key & Joins (Easy Human Language)

## What happens when we insert data into a table?

When we insert data into a table, we assign values to different columns.

Example:

```sql
INSERT INTO students (id, name, age)
VALUES (1, 'Amit', 20);
```

Here:

* `id`, `name`, and `age` are **column names**.
* `1`, `'Amit'`, and `20` are the **values** stored in those columns.

After the data is inserted, you can update or delete it later using SQL commands such as `UPDATE` or `DELETE` (unless restricted by database rules).

---

# What is a Key?

A **key** is a column (or group of columns) used to identify records and create relationships between tables.

### Why do we use keys?

* To uniquely identify each row.
* To prevent duplicate records.
* To connect multiple tables.
* To maintain data accuracy and consistency.

---

# What is a Primary Key?

A **Primary Key** is the main key of a table.

It uniquely identifies every record (row) in that table.

Think of it like your **Aadhaar Number** or **Passport Number**. Every person has a different number.

Example:

| Student_ID | Name  | Age |
| ---------- | ----- | --- |
| 101        | Amit  | 20  |
| 102        | Rahul | 21  |
| 103        | Priya | 19  |

Here, **Student_ID** is the Primary Key because every value is unique.

---

## Properties of a Primary Key

### 1. Must be Unique

Every row must have a different value.

✅ Correct

| ID |
| -- |
| 1  |
| 2  |
| 3  |

❌ Incorrect

| ID |
| -- |
| 1  |
| 1  |
| 2  |

Duplicate values are not allowed.

---

### 2. Cannot be NULL

Every record must have a value.

❌ Wrong

| ID   |
| ---- |
| NULL |
| 2    |

A Primary Key can never contain `NULL`.

---

### 3. One Primary Key per Table

A table can have only **one Primary Key**, although it can consist of multiple columns (called a composite key).

---

### 4. Auto Increment (Common Usage)

If `AUTO_INCREMENT` is used:

```sql
ID
1
2
3
```

If you delete ID = 2:

```text
1
3
```

The next inserted record becomes:

```text
4
```

The deleted ID (2) is **not reused automatically**.

> Note: This behavior is because of `AUTO_INCREMENT`, not because it is a Primary Key itself.

---

# What is a Foreign Key?

A **Foreign Key** is a column that connects one table to another.

It refers to the Primary Key of another table.

This creates a relationship between tables.

### Parent Table

Contains the Primary Key.

### Child Table

Contains the Foreign Key.

Example:

## Students Table (Parent)

| Student_ID | Name  |
| ---------- | ----- |
| 101        | Amit  |
| 102        | Rahul |

Student_ID is the Primary Key.

---

## Marks Table (Child)

| Mark_ID | Student_ID | Marks |
| ------- | ---------- | ----- |
| 1       | 101        | 95    |
| 2       | 102        | 88    |

Here, `Student_ID` is a Foreign Key because it refers to the Students table.

Relationship:

```
Students
---------
Student_ID (PK)
      │
      │
      ▼
Marks
---------
Student_ID (FK)
```

---

## Why do we use Foreign Keys?

* Connect multiple tables.
* Avoid duplicate data.
* Maintain data integrity.
* Ensure valid references between records.

---

# Parent–Child Relationship

Parent Table

```
Students
```

↓

Child Table

```
Marks
```

The child table stores the parent's Primary Key as a Foreign Key.

---

# ON DELETE CASCADE

Normally:

If a parent row is deleted while child records still exist, the database may prevent the deletion.

With `ON DELETE CASCADE`:

If the parent record is deleted, all related child records are deleted automatically.

Example

Students

| Student_ID | Name |
| ---------- | ---- |
| 101        | Amit |

Marks

| Mark_ID | Student_ID | Marks |
| ------- | ---------- | ----- |
| 1       | 101        | 95    |

Delete:

```sql
DELETE FROM Students
WHERE Student_ID = 101;
```

With `ON DELETE CASCADE`

Result:

Students

Empty

Marks

Empty

The related marks record is deleted automatically.

---

# What is a JOIN?

A **JOIN** combines data from two or more tables based on a related column.

Without JOIN:

Data stays in separate tables.

With JOIN:

You can view related information together in one result.

Example

Students

| ID | Name  |
| -- | ----- |
| 1  | Amit  |
| 2  | Rahul |

Marks

| Student_ID | Marks |
| ---------- | ----- |
| 1          | 90    |
| 2          | 80    |

JOIN Result

| ID | Name  | Marks |
| -- | ----- | ----- |
| 1  | Amit  | 90    |
| 2  | Rahul | 80    |

---

# Types of JOIN

## 1. INNER JOIN ⭐ (Most Used)

Returns only matching records from both tables.

```
Students        Marks

1 Amit      ↔   1 90
2 Rahul     ↔   2 80
3 Priya

Output

Amit
Rahul
```

Only common matching rows appear.

---

## 2. LEFT JOIN

Returns:

* All records from the left table.
* Matching records from the right table.
* If no match exists, NULL is shown.

```
Students

Amit
Rahul
Priya

Marks

Amit
Rahul

Output

Amit 90
Rahul 80
Priya NULL
```

---

## 3. RIGHT JOIN

Returns:

* All records from the right table.
* Matching records from the left table.
* If no match exists, NULL is shown.

---

## 4. FULL OUTER JOIN

Returns every record from both tables.

If there is no match, NULL is displayed on the missing side.

```
Left Table
A
B

Right Table
B
C

Output

A NULL
B B
NULL C
```

---

## 5. OUTER JOIN

An **Outer Join** returns matching records along with non-matching records.

There are three common types:

* Left Outer Join
* Right Outer Join
* Full Outer Join

These joins are useful when you want to keep unmatched rows instead of losing them.

---

# Natural JOIN

A **Natural Join** automatically joins two tables based on columns that have the same name and compatible data types.

Example:

```
Students
Student_ID

Marks
Student_ID
```

The database joins them automatically without specifying the join condition.

Use carefully, because it depends on matching column names.

---

# Cross JOIN

A **Cross Join** returns every possible combination of rows from both tables.

Example

Students

```
Amit
Rahul
```

Subjects

```
Math
English
```

Result

```
Amit  Math
Amit  English
Rahul Math
Rahul English
```

If one table has **2 rows** and the other has **3 rows**, the result contains **2 × 3 = 6 rows**.

---

# Difference Between Primary Key and Foreign Key

| Primary Key                  | Foreign Key                                |
| ---------------------------- | ------------------------------------------ |
| Uniquely identifies each row | Connects one table to another              |
| Must be unique               | Can contain duplicate values               |
| Cannot be NULL               | Can be NULL (unless restricted)            |
| One per table                | Multiple Foreign Keys can exist in a table |
| Exists in the parent table   | Exists in the child table                  |

---

# Quick Revision

* A **Key** identifies records and creates relationships.
* A **Primary Key** uniquely identifies every row.
* A **Foreign Key** links one table to another.
* **Parent Table** contains the Primary Key.
* **Child Table** contains the Foreign Key.
* **ON DELETE CASCADE** automatically deletes related child records when the parent record is deleted.
* **JOIN** combines data from multiple tables.
* **INNER JOIN** returns only matching rows.
* **LEFT JOIN** returns all left rows and matching right rows.
* **RIGHT JOIN** returns all right rows and matching left rows.
* **FULL OUTER JOIN** returns all rows from both tables.
* **NATURAL JOIN** joins tables automatically using columns with the same name.
* **CROSS JOIN** returns every possible combination of rows.

# 💻 SQL Code Examples – Keys & JOINs

# 1. Create a Database

```sql
CREATE DATABASE CollegeDB;
USE CollegeDB;
```

---

# 2. Create Students Table (Primary Key)

```sql
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Age INT,
    Email VARCHAR(100)
);
```

### Insert Data

```sql
INSERT INTO Students (Name, Age, Email)
VALUES
('Amit',20,'amit@gmail.com'),
('Rahul',21,'rahul@gmail.com'),
('Priya',19,'priya@gmail.com');
```

### View Data

```sql
SELECT * FROM Students;
```

Output

| Student_ID | Name  | Age | Email                                     |
| ---------- | ----- | --- | ----------------------------------------- |
| 1          | Amit  | 20  | [amit@gmail.com](mailto:amit@gmail.com)   |
| 2          | Rahul | 21  | [rahul@gmail.com](mailto:rahul@gmail.com) |
| 3          | Priya | 19  | [priya@gmail.com](mailto:priya@gmail.com) |

---

# 3. Update Data

```sql
UPDATE Students
SET Age = 22
WHERE Student_ID = 2;
```

---

# 4. Delete Data

```sql
DELETE FROM Students
WHERE Student_ID = 3;
```

---

# 5. Create Parent Table

```sql
CREATE TABLE Department (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(50)
);
```

Insert Data

```sql
INSERT INTO Department
VALUES
(101,'Computer Science'),
(102,'Mechanical'),
(103,'Electrical');
```

---

# 6. Create Child Table (Foreign Key)

```sql
CREATE TABLE Student_Department (

    Student_ID INT,
    Department_ID INT,

    FOREIGN KEY (Student_ID)
    REFERENCES Students(Student_ID),

    FOREIGN KEY (Department_ID)
    REFERENCES Department(Department_ID)

);
```

Insert Data

```sql
INSERT INTO Student_Department
VALUES
(1,101),
(2,102),
(3,101);
```

---

# 7. Foreign Key with ON DELETE CASCADE

```sql
CREATE TABLE Orders (

    Order_ID INT PRIMARY KEY,
    Student_ID INT,

    FOREIGN KEY (Student_ID)
    REFERENCES Students(Student_ID)
    ON DELETE CASCADE

);
```

Insert Data

```sql
INSERT INTO Orders
VALUES
(1,1),
(2,2),
(3,1);
```

Delete Student

```sql
DELETE FROM Students
WHERE Student_ID = 1;
```

Result:

All Orders having `Student_ID = 1` are deleted automatically.

---

# 8. INNER JOIN

```sql
SELECT
Students.Student_ID,
Students.Name,
Department.Department_Name

FROM Student_Department

INNER JOIN Students
ON Student_Department.Student_ID = Students.Student_ID

INNER JOIN Department
ON Student_Department.Department_ID = Department.Department_ID;
```

Output

```
1  Amit   Computer Science
2  Rahul  Mechanical
3  Priya  Computer Science
```

---

# 9. LEFT JOIN

```sql
SELECT
Students.Student_ID,
Students.Name,
Student_Department.Department_ID

FROM Students

LEFT JOIN Student_Department
ON Students.Student_ID = Student_Department.Student_ID;
```

All students are shown. If a student has no department, Department_ID will be NULL.

---

# 10. RIGHT JOIN

```sql
SELECT
Students.Student_ID,
Students.Name,
Student_Department.Department_ID

FROM Students

RIGHT JOIN Student_Department
ON Students.Student_ID = Student_Department.Student_ID;
```

All records from `Student_Department` are shown.

---

# 11. FULL OUTER JOIN

> **Note:** MySQL does **not** support `FULL OUTER JOIN` directly.

Use this alternative:

```sql
SELECT *
FROM Students
LEFT JOIN Student_Department
ON Students.Student_ID = Student_Department.Student_ID

UNION

SELECT *
FROM Students
RIGHT JOIN Student_Department
ON Students.Student_ID = Student_Department.Student_ID;
```

---

# 12. CROSS JOIN

```sql
SELECT
Students.Name,
Department.Department_Name

FROM Students

CROSS JOIN Department;
```

Output

```
Amit    Computer Science
Amit    Mechanical
Amit    Electrical
Rahul   Computer Science
Rahul   Mechanical
Rahul   Electrical
Priya   Computer Science
Priya   Mechanical
Priya   Electrical
```

---

# 13. NATURAL JOIN

Suppose two tables have the same column name (`Department_ID`).

```sql
SELECT *
FROM Student_Department
NATURAL JOIN Department;
```

MySQL automatically joins on the common column.

---

# 14. Find a Student by ID

```sql
SELECT *
FROM Students
WHERE Student_ID = 2;
```

---

# 15. Find Students Older Than 20

```sql
SELECT *
FROM Students
WHERE Age > 20;
```

---

# 16. Sort Students by Name

```sql
SELECT *
FROM Students
ORDER BY Name ASC;
```

---

# 17. Count Total Students

```sql
SELECT COUNT(*) AS Total_Students
FROM Students;
```

---

# 18. Drop a Table

```sql
DROP TABLE Student_Department;
```

---

# 19. Drop a Database

```sql
DROP DATABASE CollegeDB;
```

---

# 📌 Execution Order

```sql
CREATE DATABASE CollegeDB;

USE CollegeDB;

CREATE TABLE Students (...);

CREATE TABLE Department (...);

CREATE TABLE Student_Department (...);

INSERT INTO Students ...;

INSERT INTO Department ...;

INSERT INTO Student_Department ...;

SELECT * FROM Students;

SELECT * FROM Department;

SELECT * FROM Student_Department;

-- Practice JOINs

INNER JOIN

LEFT JOIN

RIGHT JOIN

CROSS JOIN

NATURAL JOIN
```
