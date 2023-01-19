import csv
import pandas as pd
from datetime import datetime
import hashlib
import match_category as match_c
import sqlite3

# function for createing a hashvalue
def hash_func(item1, item2, item3, item4):
    hash_string = str(item1) + str(item2) + str(item3) + str(item4)
    created_hash = hashlib.md5(hash_string.encode()).hexdigest()
    return created_hash

# function for readout file data
def create_dataframe(filename, conn, cur):

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
    # head_row = ['account_num', 'text', 'valutadate', 'amount', 'currency', 'category']
    head_row = ['hash', 'valutadate', 'amount', 'transaction_text_id', 'account_id', 'asset_class_id', 'category_in_out_id', 'currency_id', 'int_or_ext_id', 'remarks']
    bank_account_df = pd.DataFrame(columns=head_row)

    # Processes data from file
    with open(filename, 'r') as fhandle:
        csv_reader = csv.DictReader(fhandle, delimiter=';', fieldnames=header) # Adds a fieldname to the columns, so i can access them by name instead of index.

        if bank99: # Done at bank99 as there is a file header with strings in the csv
            header = next(csv_reader) # Attention, if we use this line, we define the first row in the csv file as header and don´t read it.

        # loop over data and write into dataframe
        for row_index, row in enumerate(csv_reader):

            # Safety check if all rows are equal in lenght, otherwise there could be some problem with the transformation of the data.
            # if len(row) != 6:
            #     return (f"Row {row_index} is only {len(row)} elements long.")
            #     break
            
            # Definition of data elements

            valutadate = datetime.strptime(row['valutadate'], '%d.%m.%Y')

            if bawag:
                amount = float(row['amount'].replace('.','').replace(',','.'))
            elif bank99:
                amount_withdrawal = float(row['amount_withdrawal'].replace('.','').replace(',','.'))
                amount_deposit = float(row['amount_deposit'].replace('.','').replace(',','.'))
                amount = amount_deposit - amount_withdrawal

            text = row['text']
            cur.execute('''INSERT OR IGNORE INTO Transaction_Text (transaction_text) VALUES (?)''', (text, ))
            cur.execute('''SELECT id FROM Transaction_Text WHERE transaction_text = ?''', (text, ))
            transaction_text_id = cur.fetchone()[0]
                
            account_num = row['account_num']
            cur.execute('''SELECT id FROM Accounts_Supp WHERE account_number = ?''', (account_num, ))
            try:
                account_id = cur.fetchone()[0]
            except TypeError:
                account_id = cur.fetchone()

            cur.execute('''SELECT asset_class_id FROM Accounts_Supp WHERE account_number = ?''', (account_num, ))
            try:
                asset_class_id = cur.fetchone()[0]
            except TypeError:
                asset_class_id = cur.fetchone()

            category_in_out_id = match_c.match_category(text, conn, cur)
            # print(f"Debug Printout category_in_out_id in data_readout: {category_in_out_id}")   # printour for Debug

            currency = row['currency']
            cur.execute('''SELECT id FROM Currency_Supp WHERE name = ?''', (currency, ))
            try:
                currency_id = cur.fetchone()[0]
            except TypeError:
                currency_id = cur.fetchone()

            int_or_ext_id = None

            remarks = None

            # Create hashvalue of each record, to add a uniqe identifier in the table.
            hash_val = hash_func(account_num, text, valutadate, amount)
            # print(f"Debug: {type(hash_val)}") # Printout for debug
            # hash_val = None
                        
            # Write data elements into dataframe as new row (.loc[row_index])
            bank_account_df.loc[row_index] = [hash_val, valutadate, amount, transaction_text_id, account_id, asset_class_id, category_in_out_id, currency_id, int_or_ext_id, remarks]

        # print(bank_account_df)    # Printout for debug
        # print(f"Total Rows: {row_index + 1}") # Printout for debug

    # Check for None category
    none_count_new = bank_account_df["category_in_out_id"].isnull().sum()
   
    # Return the dataframe
    return bank_account_df
    # return (f"{bank_account_df} \n Total Rows: {row_index + 1} \n None Categories: {none_count_new}") # Printout for debug
    # return (f"Total Rows: {row_index + 1}")   # Printout for debug