import mysql.connector
# connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="TotalPayment"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM customerdata")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
