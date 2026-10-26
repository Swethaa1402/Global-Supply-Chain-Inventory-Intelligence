
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter your MySQL root password: "),
    database="supply_chain_intelligence"
)

if connection.is_connected():
    print("Successfully connected to MySQL!")
    print("Database:", connection.database)

connection.close()
