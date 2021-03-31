# Python with SQL
We use PYODBC to establish a connection between Python and SQL. The PYODBC library will help us to connect to an AWS hosted database that is using SQL Server by Microsoft.

![PYTHON_SQL](https://github.com/alfonso-torres/eng84_python_with_SQL/blob/main/Python_with_SQL.png)

## Useful links to help debug PYODBC installation

- For Linux:

https://packages.microsoft.com/ubuntu/20.04/prod/pool/main/m/msodbcsql17/
https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/msodbcsql17/
- For Windows:

https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

## Establishing a connection with PYODBC
- We need to install the package pyodbc:
````commandline
pip install pyodbc
````
````python
import pyodbc # To establish a connection to a SQL using pyodbc

# Let's establish the connection using PYODBC
server = "xx.xxx.xxx.xxx" # IP address
database = "xxxx" # Name database
username = "xx" # Name of the user
password = "xxxx"
# It validates the connection for us
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Let's check if the connection has been validated and cursor object is created
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))
````
- Fetching data from the Database:
1. Fetch a single row:
````python
# Let's fetch some data from the Northwind DB
row = cursor.fetchone()
print(row)
````
2. Fetch all the rows in a query:
````python
# Let's connect to our DB and fetch some data from Customer table
cust_rows = cursor.execute("SELECT * FROM Customers").fetchall()
print(cust_rows)
# We use execute to run our queries with in a string
# fetchall() gets all the data from the table
````
3. Let's iterate through a fetchall:
````python
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
### Apply CRUD

CRUD is the acronym for "Create, Read, Update and Delete", which is used to refer to the basic functions in databases or the persistence layer in a software. Basically, the CRUD Operations in Python is written in python programming language and MySQL database.

### Making data persistent

Persistence is "the continuance of an effect after its cause is removed". In the context of storing data in a computer system, this means that the data survives after the process with which it was created has ended. In other words, for a data store to be considered persistent, it must write to non-volatile storage. Persistent data in the field of data processing denotes information that is infrequently accessed and not likely to be modified. <br/>
It means that we will always have the data in the database available anywhere in the world and whenever we want it.

# <u>SQL TASKS</u>
## Exercise: SQL OOP
This is an example of OOP using PYODBC. Create an example of how we can create services objects related to a particular table.

**__Tasks__**:

An SQL manager for the products table:
- Create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.
- As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department. The stock department may have numerous requirements, and it makes sense to contain all the requirements a code actions within a single object.
- Create two files `nw_products.py` and `nw_runner.py`. Then we will move into creating our object.

**__Extra__**:

- Apply OOP, DRY and CRUD where is possible.

**__Solutions__**:
- `nw_products.py`: We will proceed to create the product class in which we will establish the connection as well as define the variables and the corresponding methods to operate with the products table. DRY.
- `nw_runner.py`: We will start an instance of the Product class in order to use its functions and obtain the desired results. Basically a file to be able to execute the corresponding code of the Product class and to be able to play with the database (CRUD).
