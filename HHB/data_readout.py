import csv
import dataclasses
import pandas as pd
from datetime import datetime
import hashlib
import match_category as match_c

"""
# needed steps:

7) Is now specialiesed on Bawag files. need to test it also for other banks. --> Done for Bawag and Bank 99
    create a function for each bank ( Bawag, Flatex, bank99, Raika, N26)
        What is different form ing to Bawag
    the file is named after the account num. look this account num in the database and get the bank name and start the fucniton based on this.
    write data of bank into a pandas dataframe and then call a function, that writes this dataframe into the database, so we do not need to copy the database write multiple times

    Maybe the best approach is, to make all csv files the same and then send to a function to process the data.

12) Crate a early break, if the data is already in the database best before category match!!!!

"""

# function for createing a hashvalue
def hash_func(item1, item2, item3, item4):
    hash_string = str(item1) + str(item2) + str(item3) + str(item4)
    created_hash = hashlib.md5(hash_string.encode())
    return created_hash

# function for readout file data
def read_file(filename):

    bawag = False
    bank99 = False
    flatex = False
    raika = False
    n26 = False

    # Create header for data in csv
    if "Bawag" in filename:
        bawag = True
        header = ['account_num', 'text', 'date', 'valutadate', 'amount', 'currency']
    elif "bank99" in filename:
        bank99 = True
        header = ['account_num', 'text', 'valutadate', 'currency', 'amount_withdrawal', 'amount_deposit']

    # Create empty pandas dataframe for transporting data to the database
    head_row = ['account_num', 'text', 'valutadate', 'amount', 'currency', 'category']
    bank_account_df = pd.DataFrame(columns=head_row)

    # Processes data from file
    with open(filename, 'r') as fhandle:
        csv_reader = csv.DictReader(fhandle, delimiter=';', fieldnames=header) # Adds a fieldname to the columns, so i can access them by name instead of index.

        if bank99: # Done at bank99 as there is a file header with strings in the csv
            header = next(csv_reader) # Attention, if we use this line, we define the first row in the csv file as header and don´t read it.

        # loop over data and write into dataframe
        for row_index, row in enumerate(csv_reader):

            # Safety check if all rows are equal in lenght, otherwise there could be some problem with the transformation of the data.
            if len(row) != 6:
                return (f"Row {row_index} is only {len(row)} elements long.")
                break
            
            # Definition of data elements
            account_num = row['account_num']

            text = row['text']

            valutadate = datetime.strptime(row['valutadate'], '%d.%m.%Y')

            if bawag:
                amount = float(row['amount'].replace('.','').replace(',','.'))
            elif bank99:
                amount_withdrawal = float(row['amount_withdrawal'].replace('.','').replace(',','.'))
                amount_deposit = float(row['amount_deposit'].replace('.','').replace(',','.'))
                amount = amount_deposit - amount_withdrawal

            currency = row['currency']
                
            category = match_c.match_category(text)

            # Create hashvalue of each record, to add a uniqe identifier in the table.
            # hash_val = hash_func(account_num, text, valutadate, amount)

            # Write data elements into dataframe as new row (.loc[row_index])
            bank_account_df.loc[row_index] = [account_num, text, valutadate, amount, currency, category]

        # print(bank_account_df)    # Printout for debug
        # print(f"Total Rows: {row_index + 1}") # Printout for debug

    # Check for None category
    none_count_new = bank_account_df["category"].isnull().sum()
    
    return (f"{bank_account_df} \n Total Rows: {row_index + 1} \n None Categories: {none_count_new}")
    # return (f"Total Rows: {row_index + 1}")