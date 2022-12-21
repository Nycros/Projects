# Read the data from the SQL database into a dataframe 

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('HHB/Database/datadb.sqlite')
cur = conn.cursor()

# Create a dataframe for all the transactions to be stored
sql_query_trans_all = pd.read_sql_query ('''
                                SELECT
                                *
                                FROM Transactions
                                ''', conn)

# Create a dataframe for the transactions grouped  by catagory
sql_query_trans_cat = pd.read_sql_query ('''
                                SELECT
                                category_in_out_id,
                                SUM (amount)
                                FROM Transactions
                                GROUP BY category_in_out_id
                                ''', conn)

print(f"------------->> DEBUG Output of sql_query_trans_cat <<---------------------\n{sql_query_trans_cat}")

# Create a dataframe for the transactions grouped  by month
sql_query_trans_month = pd.read_sql_query ('''
                                SELECT
                                STRFTIME("%m-%Y", valutadate) AS date,
                                SUM (amount)
                                FROM Transactions
                                GROUP BY STRFTIME("%m-%Y", valutadate)
                                ''', conn)

print(f"------------->> DEBUG Output of sql_query_trans_month <<---------------------\n{sql_query_trans_month}")

# Create a dataframe  with a cumulative sum per month
df_cum_amount_month = sql_query_trans_month
df_cum_amount_month['Cumulative amount'] = sql_query_trans_month['SUM (amount)'].cumsum()

# Get category data and write into another df
sql_query_cat = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM Category_In_Out_Supp
                               ''', conn)

# Combine transactions data and catagory data into a final dataframe to access the catagory names
df_trans_cat = pd.merge(sql_query_trans_cat, sql_query_cat,
                       how='left', left_on='category_in_out_id', right_on='id')

print(f"------------->> DEBUG Output of final dataframe <<---------------------\n{df_trans_cat.head()}")

# Sum data based on column
testsum = df_trans_cat.loc[df_trans_cat['name'] == "Tanken", 'SUM (amount)'].sum()
print(f"Testsum: {testsum}")

# count values in each column
# print(df.count())




# Create data visualization

"""
# Creat single plots of data

# Plot total amount per catagory as bar chart
# df_trans_cat.plot(kind = 'barh', x = 'name', y = 'SUM (amount)')
plot = df_trans_cat.plot(kind = 'barh', x = 'name', y = 'SUM (amount)')
plot.bar_label(plot.containers[0], label_type='center')
plt.title("Total amount per category")

# Plot total amount per month as bar chart
sql_query_trans_month.plot(kind = 'barh', x = 'date', y = 'SUM (amount)')

# Plot cumulative amount per month as line chart
df_cum_amount_month.plot(kind = 'line', x = 'date', y = 'Cumulative amount')

# how to plot data: https://www.w3schools.com/python/pandas/pandas_plotting.asp
# https://data36.com/plot-histogram-python-pandas/
"""

# Show all plots in one window
"""
https://www.statology.org/pandas-subplots/
https://www.geeksforgeeks.org/change-figure-size-in-pandas-python/
https://stackoverflow.com/questions/42354515/how-to-display-a-plot-in-fullscreen
https://stackoverflow.com/questions/25239933/how-to-add-a-title-to-each-subplot
"""

#define subplot layout
# figure, axes = plt.subplots(2, 2, figsize=(20, 15)) # Create Subplots with window size 20 by 15

figure, axes = plt.subplots(2, 2)

figure.canvas.manager.full_screen_toggle() # toggle fullscreen mode

# add DataFrames to subplots
plot1 = df_trans_cat.plot(ax=axes[0,0], kind = 'barh', x = 'name', y = 'SUM (amount)')              # Plot total amount per catagory as bar chart
plot2 = sql_query_trans_month.plot(ax=axes[0,1], kind = 'barh', x = 'date', y = 'SUM (amount)')     # Plot total amount per month as bar chart
plot3 = df_cum_amount_month.plot(ax=axes[1,0], kind = 'line', x = 'date', y = 'Cumulative amount')  # Plot cumulative amount per month as line chart

# add data labels to subplots
plot1.bar_label(plot1.containers[0], label_type='center')

# add title to subplots
plot1.title.set_text('Total amount per category')
plot2.title.set_text('Total amount per month')
plot3.title.set_text('Cumulative amount per month')

plt.show()