import oracledb
import time

# Replace these with your actual values
user = "SYS"    # Your Oracle username
password = "mypassword1"  # Your Oracle password
dsn = "localhost:1521/ORCLCDB"  # DSN (e.g., "localhost:1521/orclpdb1")

# Establish the connection
connection = oracledb.connect(user=user, password=password, dsn=dsn, mode=oracledb.SYSDBA)

# Create a cursor and execute some queries
cursor = connection.cursor()

repeated_string = "abdeababababababababababababababababababababababfgrrrhq"


# SQL Insert statement
sql_insert = "INSERT INTO Q2 (Name) VALUES (:name)"

string1 = "abde"+"ab"*20+"fgrrrhq"
# string2 = "abde"+"ab"*20+"fgrrrhp"
# string3 = "abde"+"ab"*19+"afgrrrhq"
# string4 = "abda"+"ab"*19+"agrrrhq"

# Insert 'abc' 10 times using a for loop
for i in range(100000):
    cursor.execute(sql_insert, {'name': string1})
    # cursor.execute(sql_insert, {'name': string2})
    # cursor.execute(sql_insert, {'name': string3})
    # cursor.execute(sql_insert, {'name': string4})



    connection.commit()

