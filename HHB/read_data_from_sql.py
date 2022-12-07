# Read the data from the SQL database into a dataframe 

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('HHB/Database/datadb.sqlite') 

# Get transaction data and write into df  
sql_query_trans_all = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM Transactions
                               ''', conn)

# Get transactions groupt by category
sql_query_trans_cat = pd.read_sql_query ('''
                               SELECT
                               category_in_out_id,
                               SUM (amount)
                               FROM Transactions
                               GROUP BY category_in_out_id
                               ''', conn)

df_trans_all = pd.DataFrame(sql_query_trans_all, columns = ['id', 'hash', 'valutadate', 'amount', 'transaction_text_id',
                                        'account_id', 'asset_class_id', 'category_in_out_id', 'currency_id', 'int_or_ext_id', 'remarks'])

df_trans_cat = pd.DataFrame(sql_query_trans_cat, columns = ['amount', 'category_in_out_id'])

print(df_trans_cat)

# Get category data and write into another df
sql_query_cat = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM Category_In_Out_Supp
                               ''', conn)

df_cat = pd.DataFrame(sql_query_cat, columns = ['id', 'name'])
# print (df_cat)

# Combine into a final dataframe
final_df = pd.merge(df_trans_cat, df_cat,
                       how='left', left_on='category_in_out_id', right_on='id')

print(final_df.head())

# Sum data based on column
testsum = final_df.loc[final_df['name'] == 25, 'amount'].sum()
print(testsum)

# count values in each column
# print(df.count())

# Create data visualization
""" What do i want t oanalyze?
1) Income and Eypenses per month as Barchart
2) Income and Expenses per category as Barchart
3) Total account sum as linechart per month
"""
# Different Plots 
# final_df.hist(column='amount', by='name')
# df.plot.hist(column=["amount"], by="category_in_out_id")
# df.plot(kind = 'scatter', x = 'valutadate', y = 'amount')

final_df.plot(kind = 'bar', x = 'name', y = 'amount')


plt.show()

# how to plot data: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# https://data36.com/plot-histogram-python-pandas/