import sqlite3





def show_all():
    conn=sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items=c.fetchall()
    for item in items:
        print(item)
    conn.close()

def add_data(fname,lname,email):
    conn=sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items=c.fetchall()
    for item in items:
        print(item)
    c.execute("INSERT INTO customers VALUES ('{}','{}','{}')".format(fname,lname,email))

    conn.commit()
    c.execute("SELECT rowid, * FROM customers")
    items=c.fetchall()
    
    for item in items:
        print(item)
    conn.close()

# add_data('don','mallick','gmail.com')
# show_all()

