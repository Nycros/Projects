import pandas as pd
from datetime import datetime
import sqlite3

import data_readout as dr

def write_datab(file, conn, cur):
    
    # Write into Database with a for loop
    # Get the dataframe
    data_frame = dr.create_dataframe(file, conn, cur)
    # print(f"Debug printout dataframe from write_database: {data_frame}")  # PRintout for Debug

    # Write all data into SQL tabel
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

    # Update all the older rows witth new data
    for index, row in data_frame.iterrows():
        cur.execute('''
                    UPDATE
                    Transactions
                    SET valutadate = ?, amount = ?, transaction_text_id = ?, account_id = ?, asset_class_id = ?, category_in_out_id = ?, currency_id = ?, 
                    int_or_ext_id = ?
                    WHERE hash = ?
                    ''', 
                    (str(row['valutadate']), row['amount'],
                    row['transaction_text_id'], row['account_id'], row['asset_class_id'],
                    row['category_in_out_id'], row['currency_id'], row['int_or_ext_id'], str(row['hash'])))    