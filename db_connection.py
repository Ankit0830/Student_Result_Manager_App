import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "student_result_manager"
)

cursor = conn.cursor()

# print("Connected Successfully!")