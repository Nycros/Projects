import pandas as pd
from datetime import datetime
import sqlite3

import data_readout as dr

def write_datab(file, conn, cur):
    """
    # First try, but problem is, that the data will be appended and not updated
    cur.executescript('''
    DROP TABLE IF EXISTS myTempTable;
    CREATE TABLE myTempTable (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        hash Text,
        valutadate DATE,
        amount FLOAT,
        transaction_text_id INTEGER,
        account_id INTEGER,
        asset_class_id INTEGER,
        category_in_out_id INTEGER,
        currency_id INTEGER,
        int_or_ext_id INTEGER,
        remarks Text
    )''')

    # Get the dataframe
    data_frame = dr.create_dataframe(file, conn, cur)
    # Add an id column at the beginnig of the dataframe so the column numbers fit to the sql table
    data_frame.insert (0, "id", None)

    # Write the dataframe into a tamporary table. Please make sure, the number of columns fit to the columns of the Transacions table.
    data_frame.to_sql('myTempTable', conn, if_exists='append', index = False)

    # Transmit from the temporary tabel to the final tabel
    cur.execute("INSERT OR IGNORE INTO Transactions SELECT * FROM myTempTable")
    """

    
    # Write into Database with a for loop
    # Get the dataframe
    data_frame = dr.create_dataframe(file, conn, cur)

    for index, row in data_frame.iterrows():
        cur.execute('''
                    INSERT OR IGNORE INTO
                    Transactions
                    (hash, valutadate, amount, transaction_text_id, account_id, asset_class_id, category_in_out_id, currency_id, int_or_ext_id, remarks)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', 
                    (str(row['hash']), str(row['valutadate']), row['amount'],
                    row['transaction_text_id'], row['account_id'], row['asset_class_id'],
                    row['category_in_out_id'], row['currency_id'], row['int_or_ext_id'], row['remarks']))    