import mysql.connector
from db import execute_query, create_db_connection


def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

connection = create_db_connection("localhost", "root", "password", "db")

cursor = connection.cursor()
sql_fetch_blob_query = """SELECT * from pokemon where id = %s"""

cursor.execute(sql_fetch_blob_query, (emp_id,))
record = cursor.fetchall()
for row in record:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    image = row[2]
    file = row[3]
    print("Storing employee image and bio-data on disk \n")
    write_file(image, photo)
    write_file(file, bioData)