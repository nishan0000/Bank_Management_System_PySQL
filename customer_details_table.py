# This python file is used to create a customer_details table which is used to store all teh details of every customers
# of the bank

# Importing mysql library.
import mysql.connector as sql

# Connecting to the database using local credentials.
mydb = sql.connect(host='localhost',user='root',password='0007',database='bank1')


# Creating a cursor to execute the SQL Queries.
cursor = mydb.cursor()
cursor.execute('create table customer_details(acc_no int primary key,acc_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float )')
