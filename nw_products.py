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
