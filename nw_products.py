import pyodbc

class Products:

    def __init__(self):
        # Let's establish the connection using PYODBC
        server = "xxxxxxx"
        database = "xxxxxx"
        username = "xxxxx"
        password = "xxxxxxxxxx"
        docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.__cursor = docker_Northwind.cursor()
        # self.__cursor.execute("SELECT @@version;")
        # row = self.__cursor.fetchone()
        self.rows = self.__createtable()

    # create a function to fetch all the unit prices from the Product table
    def fetch_unitprice(self):
        row = self.__cursor.execute("SELECT * FROM Products")
        while True:
            record = row.fetchone()
            if record is None:
                break
            print(record.UnitPrice)

    # Function to duplicate the table Products to operate with this new table
    def __createtable(self):
        try:
            return self.__cursor.execute(f"SELECT * FROM jose_table").fetchall()
        except:
            self.__cursor.execute("SELECT * INTO jose_table FROM Products")
        finally:
            return self.__cursor.execute("SELECT * FROM jose_table").fetchall()

    # Function to close the connection
    def close_connection(self):
        self.__cursor.close()

    # Function to count how many products there are for UnitsInStocks
    def count_product(self, product_name):
        row = self.__cursor().execute(f"SELECT UnitsInStock FROM jose_table WHERE ProductName = '{product_name}'").fetchone()
        if row is None:
            return "Sorry there is not units."
        else:
            row[0]

    # Function to update stocks to a product
    def update_product(self, product_name, count):
        count_now = self.count_product(product_name)
        count_total = count_now + count
        self.__cursor.execute(f"UPDATE jose_table SET UnitsInStock={count_total} WHERE ProductName = '{product_name}'")

    # Function to subtract units in a product
    def subtract_product_stock(self, product_name, count):
        self.add_product_stock(product_name, -count)

    # Function to delete a product in the table
    def delete_product(self, product_name):
        self.__cursor.execute(f"DELETE FROM jose_table WHERE ProductName = '{product_name}'")
