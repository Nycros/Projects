import csv
import matplotlib.pyplot as plt
import numpy as np
import sqlite3


# 1) create tabel in database
# 2) read data from excel
# 3) write data into database

# Create connection to database and tables
conn = sqlite3.connect('HHB/datadb.sqlite')
cur = conn.cursor()

# Create tables in the database
cur.executescript('''
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS I_O;
DROP TABLE IF EXISTS Bank;

CREATE TABLE Accounts (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    iban    TEXT UNIQUE,
    name    TEXT,
    bank_id
);

CREATE TABLE Bank (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE I_O (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    text    TEXT,
    valutadate  DATE,
    currency TEXT,
    withdrawal FLOAT,
    deposit FLOAT,
    account_id INTEGER
);
''')

# Read data from csv
acc_file = ('HHB/Bawag.csv')

fhandle = open(acc_file, 'r')
csv_reader = csv.reader(fhandle)
header = next(csv_reader)

# loop over data and write into database
for count, row in enumerate(csv_reader):

    # Assign Varialbes
    iban = row[0]
    text = row[1]
    valutadate = row[2]
    currency = row[3]
    withdrawal = float(row[4])
    deposit = float(row[5])

    # Write the IBAN into the accounts table and pulls out the account id for the next table
    cur.execute('''INSERT OR IGNORE INTO Accounts (iban)
        VALUES ( ? )''', ( iban, ) )
    cur.execute('SELECT id FROM Accounts WHERE iban = ? ', (iban, ))
    account_id = cur.fetchone()[0]

    # Write data to the I_O table
    cur.execute('''INSERT OR REPLACE INTO I_O
        (text, valutadate, currency, withdrawal, deposit, account_id)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( text, valutadate, currency, withdrawal, deposit, account_id ) )

# print the whole I_O table
# cur.execute('''SELECT * FROM I_O''')
# print(cur.fetchall())

# print only the sum of the withdrawal of the I_O table
cur.execute('''SELECT SUM(withdrawal) FROM I_O''')
print(f'Total Withdrawal {cur.fetchall()}')

conn.commit()

fhandle.close()
