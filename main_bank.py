# When this application is ran, the user have two options.
# 1. Register - if new user
# 2. Login - if existing user
# This python file is used to ask the user if the user is a new user or an existing user.


# Importing the mysql library as sql
import mysql.connector as sql
# Importing datetime library as dt
import datetime as dt

# connecting to mySQL database using the local credentilas
mydb = sql.connect(host='localhost',user='root',password='0007',database='bank1')

# Crerating a cursor to execute the SQL queries
cursor = mydb.cursor()

print('=========================WELCOME TO BANK OF INDIA============================================================')
print(dt.datetime.now())
print('-------------------------------')
# Printing the available types of sign-in methods
print('1. REGISTER')
print()
print('2. LOGIN')
print()

# Ask the user to choose a type of sign in
n = int(input("Enter your choice : "))

# If the user choose to Register a new user
if n == 1:
    print('----------------------------')
    # Ask for a new username
    name = input("Enter A Username : ")
    print()
    # Ask for a new password
    password = input("Enter A 4 Digit Password : ")
    print()
    # Insert both of the username and password data to the table
    nmps_tbl = f"INSERT INTO user_table (username,password) values ('{str(name)}','{str(password)}') "
    cursor.execute(nmps_tbl)
    mydb.commit()
    # If everything goes correct, print successful
    print("Sign Up Successful")
    import menu

# If the user choose to Login an existing user
elif n == 2:
    print('----------------------------')
    # Ask for existing username
    name = input("Enter Your Username : ")
    print()
    # Ask for existing password
    password = input("Enter Your 4 Digit Password : ")
    print()
    # Check if the username and password data is available inside the database
    chk_tbl = f"SELECT * FROM user_table WHERE username='{str(name)}' AND password='{str(password)}'"
    cursor.execute(chk_tbl)
    # If data is not found inside the database, print invalid username
    if cursor.fetchone() is None:
        print()
        print("Invalid Username Or Password")
    else:
        # If credentials are correct, print successful
        print("Login Successful")
        import menu
