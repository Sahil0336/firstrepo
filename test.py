import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12121122"
)

print(mydb)