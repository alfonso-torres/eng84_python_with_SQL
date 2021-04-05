from nw_products import Products

cursor = Products()

# Get all the rows from the products table
print(cursor.rows)

# fetch all the unit prices from the Product table
print(cursor.fetch_unitprice())

# Let's check the stock of one product
print(cursor.count_product("CHECK_THE_TABLE_FIRSTLY_PLEASE"))

# Let's add some units to one product
cursor.update_product("CHECK_THE_TABLE_FIRSTLY_PLEASE", 4)

# Let's check if it was modified
print(cursor.count_product("CHECK_THE_TABLE_FIRSTLY_PLEASE"))

# Let's go to delete the product
cursor.delete_product("CHECK_THE_TABLE_FIRSTLY_PLEASE")

# Let's check if it was deleted
print(cursor.count_product("CHECK_THE_TABLE_FIRSTLY_PLEASE"))

# Close the connection
cursor.close_connection()
