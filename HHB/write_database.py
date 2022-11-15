import pandas as pd
import sqlite3

import data_readout as dr

def write_datab(file, conn, cur):

    cur.executescript('''
    DROP TABLE IF EXISTS myTempTable;
    CREATE TABLE myTempTable (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        hash INTEGER,
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
    data_frame.to_sql('myTempTable', conn, if_exists='replace', index = False)

    # Transmit from the temporary tabel to the final tabel
    cur.execute("INSERT OR IGNORE INTO Transactions SELECT * FROM myTempTable")


    # The problem is, the data will stil be appeded and not updated