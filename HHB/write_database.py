import pandas as pd
import sqlite3

import data_readout as dr

def write_datab(file):
    # Create connection to database and tables
    conn = sqlite3.connect('HHB/Database/datadb.sqlite')
    cur = conn.cursor()

    # Get the dataframe
    data_frame = dr.create_dataframe(file)

    data_frame.to_sql('Transactions', conn, if_exists='append', index = False)

    conn.commit()