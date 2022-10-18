import sqlite3

# Create connection to database and tables
conn = sqlite3.connect('HHB/datadb.sqlite')
cur = conn.cursor()

# select all elements form for "name"
cur.execute("SELECT name FROM Catagory_In_Out")

# fetch all the matching rows 
all_cat = cur.fetchall()

print(all_cat)

# Readout each row of the column name
for catagory in all_cat:
    print(catagory[0])