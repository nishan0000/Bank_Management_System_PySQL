# This python file is used to create a table which is used to store the details of transactions happening in the
# accounts

# Importing mysql library.
import mysql.connector as sql

# Connecting to the database using local credentials.
mydb = sql.connect(host='localhost',user='root',password='0007',database='bank1')


# Creating a cursor to execute the SQL Queries.
cursor = mydb.cursor()

# Creating a table named transactions to store the transaction data
transact_table = "CREATE TABLE transactions(acc_no int(11),date date,withdrawal_amt bigint(20),deposit_amt bigint(20));"
cursor.execute(transact_table)

print("Table transactions created successfuly")