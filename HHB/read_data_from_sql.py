# Read the data from the SQL database into a dataframe 

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('HHB/Database/datadb.sqlite') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM Transactions
                               ''', conn)

df = pd.DataFrame(sql_query, columns = ['id', 'hash', 'valutadate', 'amount', 'transaction_text_id',
                                        'account_id', 'asset_class_id', 'category_in_out_id', 'currency_id', 'int_or_ext_id', 'remarks'])
# print (df)

# Sum data based on column
testsum = df.loc[df['category_in_out_id'] == 25, 'amount'].sum()
print(testsum)

df.hist(column='amount', by='category_in_out_id')
df.plot.hist(column=["amount"], by="category_in_out_id")

plt.show()

# how to plot data: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# https://data36.com/plot-histogram-python-pandas/