# Making a database with sqlit3 & Python

import sqlite3

# Connect to database object

# If database doesnt exist create it
conn = sqlite3.connect('employee_info.db')
cur = conn.cursor()
print "Opened database successfully";

# Drop table if it'll already exist
cur.execute('''
DROP TABLE IF EXISTS employees''')

# Create a table
# Give name a value type of TEXT(string)
# Give age value type of int
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS employees(name TEXT, age INTEGER)')

# Input/insert data into table

def data_entry():
    cur.execute("INSERT INTO employees VALUES('Dave', 34)")

    cur.execute("INSERT INTO employees VALUES('Kelly', 27)")
    conn.commit()
    cur.close()
    conn.close()

create_table()
data_entry()




