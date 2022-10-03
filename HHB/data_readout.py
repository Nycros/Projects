import csv
import pandas as pd

"""
# needed steps:
1) add header --> Done
2) read data --> Done
3) check if all rows are equal in length --> Done
4) transform data
    account num
    text
    date    --> date
    date    --> date
    amount  --> float
    currency
5) write data into database

Is now specialiesed on Bawag files. need to test it also for other banks.
"""

# Read data from csv
acc_file = ('HHB/Bawag.csv')
header = ['account_num', 'text', 'date', 'valutadate', 'amount', 'currency']

with open(acc_file, 'r') as fhandle:
    csv_reader = csv.DictReader(fhandle, delimiter=';', fieldnames=header) # Adds a fieldname to the columns, so i can access them by name instead of index.
    # header = next(csv_reader) # Attention, if we use this line, we define the first row in the csv file as header and don´t read it.
    # print(header)

    # loop over data and print it
    tot_amount = 0
    for count, row in enumerate(csv_reader):

        # Safety check if all rows are equal in lenght, otherwise there could be some problem with the transformation of the data.
        if len(row) != 6:
            print(f"Row {count} is only {len(row)} elements long.")
            break
        
        # Definition of data elements
        account_num = row['account_num']
        text = row['text']
        date = row['date']
        valutadate = row['valutadate']
        amount = float(row['amount'].replace('.','').replace(',','.'))
        currency = row['currency']

        # print(f"account_num: {account_num}; text: {text}; date: {date}; valutadate: {valutadate}; amount: {amount}; currency: {currency}")

    print(f"Total Rows: {count}")

