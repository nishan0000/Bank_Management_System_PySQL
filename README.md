# Bank_Management_System Using SQL+Python

This is a project which is basically intended to connect python with mySQL database and create a bank management system which works like a real bank management system,it have mainly 3 tables and they are : 
* customer_details_table : used to store customer data.
* transactions : used to store the transaction history.
* user_table : used to store the username and password of the users.

### There are basically 2 functions when it comes to the first part,

#### 1. Sign-Up to the app
#### 2. Login to the app

If the user exists, they can login, and if dont exist, they have to sign-up

After logging in to the application,there are basically 6 operations or functions which can be performed
#### 1. Create a bank account
#### 2. Initiate a transaction
#### 3. Show Customer details
#### 4. Show transaction details
#### 5. Delete Bank account
#### 6. Quit

1. Create a bank account : If the user selects choice 1 or to create a bank account, a new bank account will be created and the customer details like acc_no, acc_name, 
phone_no, address, cr_amt will be stored in the customer_details table.

2. Initiate a transaction : If the user selects choice 2 or to initiate a transaction, they will be prompted to select either deposit or withdrawal
and depending upon the operation or the mode of transaction they need, the transaction amount will be added or deducted from the customer_details cr_amount colummn and
will also be recorded in the transactions table.

3. Show Customer details : If the user selects choice 3 or to show customer details, Account_Number, Account_Name, Phone_Number, Address and Balance_Amount of that particular 
user will be displayed.

4. Show transaction details : If the user selects choice 4 or to show the transaciton details assosciated with that particular account, Account_Number, Transaction_Date, 
Withdrawal-Amount and Deposit_Amount details related to that particular account will be displayed.

5. Delete Bank account : If the user selects the choice 5 or to delete the bank account, The bank account assosciated with that particular account number will be deleted

6. Quit : If the user selects the choice 6 , The application quits.
