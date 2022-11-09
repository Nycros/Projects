import pandas as pd
import sqlite3

import data_readout as dr

def write_datab(file):
    # Create connection to database and tables
    conn = sqlite3.connect('HHB/datadb.sqlite')
    cur = conn.cursor()

    # Get the dataframe
    data_frame = dr.create_dataframe(file)

    
    data_frame.to_sql('products', conn, if_exists='replace', index = False)

    conn.commit()