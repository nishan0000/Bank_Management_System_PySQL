# This python file is used to create the user_table which is used to store the users details like
# Username and Password.

# Importing mysql library.
import mysql.connector as sql

# Connecting to the database using local credentials.
mydb = sql.connect(host='localhost',user='root',password='0007')


# Creating a cursor to execute the SQL Queries.
cursor = mydb.cursor()


# Creating a database named as bank.
#bank_db = 'CREATE DATABASE bank1'
#cursor.execute(bank_db)

# Selecting the created database for further use.
cursor.execute("USE bank1")

# Creating a table named user_table to store the username and password data.
user_table = "CREATE TABLE user_table(username varchar(50) primary key,password varchar(25) not null)"
cursor.execute(user_table)


print("Table user_table created successfuly")
