from nw_products import Products

cursor = Products()

# Get all the rows from the products table
print(cursor.rows)

# fetch all the unit prices from the Product table
print(cursor.fetch_unitprice())

# Close the connection
cursor.close_connection()
