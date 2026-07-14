import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amitkumar1231@",
    database="studentdb"
)

print("Connected Successfully!")

# Create cursor
cursor = connection.cursor()

sql = """
INSERT INTO Students(Name, Email, Mobile)
VALUES (%s, %s, %s)
"""

values = (
    "Amit",
    "amit@gmail.com",
    "9876543210"
)

cursor.execute(sql, values)

connection.commit()

print("Student Added Successfully!")

cursor.close()
connection.close()