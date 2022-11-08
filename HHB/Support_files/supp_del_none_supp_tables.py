# Deleteing all tables, which are filled by the code readout from a csv/ file

import sqlite3

if __name__ == "__main__":
    # Create connection to database and tables
    conn = sqlite3.connect('HHB/Database/datadb.sqlite')
    cur = conn.cursor()

    # Create tables in the database
    cur.executescript('''
    DELETE FROM Categories_Match;
    DELETE FROM Transaction_Text;
    DELETE FROM Transactions;
    ''')

    conn.commit()