-- DROP DATABASE IF EXISTS databaseOne;
-- CREATE DATABASE databaseOne;
-- USE databaseOne;

-- CREATE TABLE tableone (
-- ID INT,
-- UNAME VARCHAR(100),
-- MOBILE VARCHAR(100),
-- EMAIL VARCHAR(100)
-- );

-- INSERT INTO tableone (ID, UNAME, MOBILE, EMAIL) VALUES 
-- ( '1', 'NAMEONE', '9847334523', 'amit1@gmail.com'),
-- ( '2', 'NAMETWO', '98424334529', 'amit2@gmail.com'),
-- ( '3', 'NAMETHREE', '98463345256', 'amit3@gmail.com'),
-- ( '4', 'NAMEFOUR', '9847384522', 'amit4@gmail.com'),
-- ( '5', 'NAMEFIVE', '9847284521', 'amit5@gmail.com');

-- SELECT * FROM tableone
-- WHERE ID = 3;



CREATE TABLE employee_demographics (
  employee_id INT NOT NULL,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  age INT,
  gender VARCHAR(10),
  birth_date DATE,
  PRIMARY KEY (employee_id)
);

CREATE TABLE employee_salary (
  employee_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  occupation VARCHAR(50),
  salary INT,
  dept_id INT
);


INSERT INTO employee_demographics (employee_id, first_name, last_name, age, gender, birth_date)
VALUES
(1,'Leslie', 'Knope', 44, 'Female','1979-09-25'),
(3,'Tom', 'Haverford', 36, 'Male', '1987-03-04'),
(4, 'April', 'Ludgate', 29, 'Female', '1994-03-27'),
(5, 'Jerry', 'Gergich', 61, 'Male', '1962-08-28'),
(6, 'Donna', 'Meagle', 46, 'Female', '1977-07-30'),
(7, 'Ann', 'Perkins', 35, 'Female', '1988-12-01'),
(8, 'Chris', 'Traeger', 43, 'Male', '1980-11-11'),
(9, 'Ben', 'Wyatt', 38, 'Male', '1985-07-26'),
(10, 'Andy', 'Dwyer', 34, 'Male', '1989-03-25'),
(11, 'Mark', 'Brendanawicz', 40, 'Male', '1983-06-14'),
(12, 'Craig', 'Middlebrooks', 37, 'Male', '1986-07-27');


INSERT INTO employee_salary (employee_id, first_name, last_name, occupation, salary, dept_id)
VALUES
(1, 'Leslie', 'Knope', 'Deputy Director of Parks and Recreation', 75000,1),
(2, 'Ron', 'Swanson', 'Director of Parks and Recreation', 70000,1),
(3, 'Tom', 'Haverford', 'Entrepreneur', 50000,1),
(4, 'April', 'Ludgate', 'Assistant to the Director of Parks and Recreation', 25000,1),
(5, 'Jerry', 'Gergich', 'Office Manager', 50000,1),
(6, 'Donna', 'Meagle', 'Office Manager', 60000,1),
(7, 'Ann', 'Perkins', 'Nurse', 55000,4),
(8, 'Chris', 'Traeger', 'City Manager', 90000,3),
(9, 'Ben', 'Wyatt', 'State Auditor', 70000,6),
(10, 'Andy', 'Dwyer', 'Shoe Shiner and Musician', 20000, NULL),
(11, 'Mark', 'Brendanawicz', 'City Planner', 57000, 3),
(12, 'Craig', 'Middlebrooks', 'Parks Director', 65000,1);



CREATE TABLE parks_departments (
  department_id INT NOT NULL AUTO_INCREMENT,
  department_name varchar(50) NOT NULL,
  PRIMARY KEY (department_id)
);

INSERT INTO parks_departments (department_name)
VALUES
('Parks and Recreation'),
('Animal Control'),
('Public Works'),
('Healthcare'),
('Library'),
('Finance');



SELECT * FROM employee_demographics
WHERE gender = 'Female';











table_references:
    table_reference [, table_reference] ...

table_reference:
    table_factor
  | join_table

table_factor:
    tbl_name [[AS] alias] [index_hint_list]
  | table_subquery [AS] alias
  | ( table_references )
  | { OJ table_reference LEFT OUTER JOIN table_reference
        ON conditional_expr }

join_table:
    table_reference [INNER | CROSS] JOIN table_factor [join_condition]
  | table_reference STRAIGHT_JOIN table_factor
  | table_reference STRAIGHT_JOIN table_factor ON conditional_expr
  | table_reference {LEFT|RIGHT} [OUTER] JOIN table_reference join_condition
  | table_reference NATURAL [{LEFT|RIGHT} [OUTER]] JOIN table_factor

join_condition:
    ON conditional_expr
  | USING (column_list)

index_hint_list:
    index_hint [, index_hint] ...

index_hint:
    USE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
  | IGNORE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] (index_list)
  | FORCE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] (index_list)

index_list:
    index_name [, index_name] ...

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
