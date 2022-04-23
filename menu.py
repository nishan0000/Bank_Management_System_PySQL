# After logging in to the application, we have basically 6 functions which can be performed
# 1. Create a bank account
# 2. Initiate a transaction
# 3. Show Customer details
# 4. Show transaction details
# 5. Delete Bank account
# 6. Quit
# This python file is used to perform all of these functions and store the data to respective databases

# Importing the mysql and datetime libraries from python as sql and dt respecctively
import datetime

import mysql.connector as sql
import datetime as dt

# Connecting to the desired database here, it is bank1
mydb = sql.connect(host='localhost',user='root',password='0007',database='bank1')

# Creating a cursor to execute SQL Queries
cursor = mydb.cursor()
# Turning the autocommit to True/ON
mydb.autocommit = True

# Storing todays date to a variable
date = datetime.date.today()


# To run the while loop as many times as we need
while True:
    # Printing all the available functions which can be done using the application.
    print()
    print('1. Create A Bank Account')
    print()
    print('2. Initiate A Transaction')
    print()
    print('3. Show Customer Details')
    print()
    print('4. Show Transaction Details')
    print()
    print('5. Delete Bank Account')
    print()
    print('6. Quit The Application')
    print()

    # Asking the user to choose a function from the given above list
    n = int(input("Enter Your Choice : "))
    print()

    # If the selected Choice is 1 / To Create A Bank Account.
    if n == 1:
        # Asking the user to enter a
        acc_no = int(input("Enter Your Account Number : "))
        print()
        acc_name = input("Enter Your Account Name : ")
        print()
        phone_no = int(input("Enter Your Phone Number : "))
        print()
        address = input("Enter Your Location : ")
        print()
        cr_amt = float(input("Enter The Amount To Be Credited : "))
        print()

        insrt_data_1 = f"INSERT INTO customer_details(acc_no, acc_name, phone_no, address, cr_amt) values('{int(acc_no)}', '{str(acc_name)}', '{int(phone_no)}', '{str(address)}', '{float(cr_amt)}')"
        cursor.execute(insrt_data_1)
        mydb.commit()
        print("====== Account Created Successfully ======")

    # If the selected Choice is 2 / To Initiate A Transaction.
    elif n == 2:
        # Asking the user for Account Number
        acc_no = int(input("Enter Your Account Number : "))
        # Check if the account number is present inside the customer_details table.
        acc_no_qr = f"SELECT * FROM customer_details WHERE acc_no = '{int(acc_no)}'"
        cursor.execute(acc_no_qr)
        data = cursor.fetchall()
        # Counting the rows of the result of above query to validate the account presence
        count = cursor.rowcount
        mydb.commit()

        # If Account not present, print account not found
        if count == 0:
            print()
            print("Account Not Found, Create One")
            print()

        # If account found, two operations can be done
        # 1. Deposit
        # 2. Withdraw
        else:
            print()
            print("1. Deopsit Money")
            print()
            print("2. Withdraw Money")
            print()
            print()

            x = int(input("Enter Your Choice : "))
            print()
            if x == 1:
                dep_amt = float(input("Enter Amount To Deposit : "))
                wd_amt = 0
                dep_qry = f"UPDATE customer_details SET cr_amt = cr_amt + '{float(dep_amt)}' WHERE acc_no = '{int(acc_no)}'"
                cursor.execute(dep_qry)
                trans_qry = f"INSERT INTO transactions(acc_no, date, withdrawal_amt, deposit_amt) values('{int(acc_no)}','{date}','{wd_amt}','{float(dep_amt)}')"
                cursor.execute(trans_qry)
                mydb.commit()
                print("Amount Deposited And Updated Successfully")
            elif x == 2:
                wd_amt = float(input("Enter Amount To Withdraw : "))
                dep_amt = 0
                wd_qry = f"UPDATE customer_details SET cr_amt = cr_amt - '{float(wd_amt)}' WHERE acc_no = '{int(acc_no)}'"
                cursor.execute(wd_qry)
                mydb.commit()
                trans_qry = f"INSERT INTO transactions(acc_no, date, withdrawal_amt, deposit_amt) values('{int(acc_no)}','{date}','{float(wd_amt)}','{dep_amt}')"
                cursor.execute(trans_qry)
                mydb.commit()
                print("Amount Withdrawn And Updated Successfully")


