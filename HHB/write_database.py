import pandas as pd
import sqlite3

import data_readout as dr

def write_datab(file, conn, cur):

    # Get the dataframe
    data_frame = dr.create_dataframe(file, conn, cur)

    data_frame.to_sql('Transactions', conn, if_exists='append', index = False)