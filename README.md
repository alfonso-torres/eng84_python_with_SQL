# Python with SQL
## Estableshing a connection with PYODBC
### Apply CRUD
### Making data persistent

````python
import pyodbc

# Let's establish the connection using PYODBC
server = "18.135.103.95"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
# It validates the connection for us
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Let's check if the connection has been validated and cursor object is created
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))

# Let's fetch some data from the Northwind DB
row = cursor.fetchone()
print(row)

# Let's connect to our DB and fetch some data from Customer table
cust_rows = cursor.execute("SELECT * FROM Customers").fetchall()
print(cust_rows)
# We use execute to run our queries with in a string
# fetchall() gets all the data from the table

# Let's iterate through the Product Table and check the UnitPrices available
prod_rows = cursor.execute("SELECT * FROM Products").fetchall()
for records in prod_rows:
    print(records.UnitPrice)

row = cursor.execute("SELECT * FROM Products")
while True:
    record = row.fetchone()
    if record is None:
        break
    print(record.UnitPrice)
````
## Useful links to help debug PYODBC installation
- For Linux:

https://packages.microsoft.com/ubuntu/20.04/prod/pool/main/m/msodbcsql17/
https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/msodbcsql17/
- For Windows:

https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
# <u>SQL TASKS</u>
