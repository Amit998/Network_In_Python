import sqlite3

# conn=sqlite3.connect(':memory:')

#connect DB
conn=sqlite3.connect('customer.db')

#create Cursor
c= conn.cursor()

#Create a table

# c.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text,
#     email text
# )""")


# many_customers=[
#     ('David','William','Dv@gmail.com'),
#     ('Sunil','Chettri','Sunil@gmail.com'),
#     ('MS','Dhoni','Dhoni@gmail.com')
# ]
# c.execute("INSERT INTO customers VALUES ('Shirley','Setia','Shetiya@gmail.com')")

# c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

# c.execute("SELECT rowid, * FROM customers")
# c.execute("SELECT * FROM customers WHERE email LIKE '%@gmail.com'  ")

#UPDATE
# c.execute("""
# UPDATE customers SET first_name ='AMit' WHERE last_name='William' 
# """)

# c.execute("DELETE from customers WHERE last_name='Dhoni' ")
# c.execute("DELETE from customers WHERE rowid=1 ")

# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

# c.execute("SELECT * from customers WHERE rowid= 1 AND last_name LIKE 'D%' ")
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid LIMIT 2")
# c.execute("DROP TABLE customers")

# print(c.fetchall())
# c.fetchmany(3)
# print(c.fetchone()[0])
items=c.fetchall()

# print(items)

# print("NAME \t\t\t EMAIL")
print("-"*40)
for item in items:
    # print(item[0] +" "+ item [1]+" \t\t "+item[2])
    print(item)

print("Command Executed Succesfully")

#commit our command
conn.commit()

#Close Our Connection
conn.close()