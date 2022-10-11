import csv
import pandas as pd
from datetime import datetime
import hashlib
import os

"""
# needed steps:
1) add header --> Done
2) read data --> Done
3) check if all rows are equal in length --> Done
4) transform data --> Done
    account num
    text
    date    --> date
    date    --> date
    amount  --> float
    currency
5) Create hash value --> done
6) read data form folder not only from file --> Done
7) Is now specialiesed on Bawag files. need to test it also for other banks.
    create a function for each bank ( Bawag, Flatex, Ing Diba, Raika, )
    the file is named after the account num. look this account num in the database and get the bank name and start the fucniton based on this.

6) write data into database 
    Use INSERT OR IGNORE
    MAybe HAsh value is not neccessary if it is checked all values

"""


# function for createing a hashvalue
def hash_func(item1, item2, item3, item4):
    hash_string = str(item1) + str(item2) + str(item3) + str(item4)
    created_hash = hashlib.md5(hash_string.encode())
    return created_hash


# function for readout bawag data
def read_bawag(filename):
    # Create header for data in csv
    header = ['account_num', 'text', 'date', 'valutadate', 'amount', 'currency']

    with open(filename, 'r') as fhandle:
        csv_reader = csv.DictReader(fhandle, delimiter=';', fieldnames=header) # Adds a fieldname to the columns, so i can access them by name instead of index.
        # header = next(csv_reader) # Attention, if we use this line, we define the first row in the csv file as header and don´t read it.
        # print(header)

        # loop over data and print it
        for count, row in enumerate(csv_reader):

            # Safety check if all rows are equal in lenght, otherwise there could be some problem with the transformation of the data.
            if len(row) != 6:
                print(f"Row {count} is only {len(row)} elements long.")
                break
            
            # Definition of data elements
            account_num = row['account_num']
            text = row['text']
            date = datetime.strptime(row['date'], '%d.%m.%Y')
            valutadate = datetime.strptime(row['valutadate'], '%d.%m.%Y')
            amount = float(row['amount'].replace('.','').replace(',','.'))
            currency = row['currency']

            # Create hashvalue of each record, to add a uniqe identifier in the table.
            hash_val = hash_func(account_num, text, valutadate, amount)

            print(f"hash: {hash_val.hexdigest()}; account_num: {account_num}; text: {text}; date: {date}; valutadate: {valutadate}; amount: {amount}; currency: {currency}")

        print(f"Total Rows: {count + 1}")


# create a list of files in the folder
folder = "HHB/Bank_statements"
all_files = os.listdir(folder)


# Read data from all csv fiels one after another
for file in all_files:
    if file.endswith(".csv") and file.startswith("Bawag"):
        # Concatenating the file name with the folder
        acc_file = folder + "/" + file
        read_bawag(acc_file)











"""
# backup for file readout
        # Create header for data in csv
        header = ['account_num', 'text', 'date', 'valutadate', 'amount', 'currency']

        with open(acc_file, 'r') as fhandle:
            csv_reader = csv.DictReader(fhandle, delimiter=';', fieldnames=header) # Adds a fieldname to the columns, so i can access them by name instead of index.
            # header = next(csv_reader) # Attention, if we use this line, we define the first row in the csv file as header and don´t read it.
            # print(header)

            # loop over data and print it
            for count, row in enumerate(csv_reader):

                # Safety check if all rows are equal in lenght, otherwise there could be some problem with the transformation of the data.
                if len(row) != 6:
                    print(f"Row {count} is only {len(row)} elements long.")
                    break
                
                # Definition of data elements
                account_num = row['account_num']
                text = row['text']
                date = datetime.strptime(row['date'], '%d.%m.%Y')
                valutadate = datetime.strptime(row['valutadate'], '%d.%m.%Y')
                amount = float(row['amount'].replace('.','').replace(',','.'))
                currency = row['currency']

                # Create hashvalue of each record, to add a uniqe identifier in the table.
                hash_val = hash_func(account_num, text, valutadate, amount)

                print(f"hash: {hash_val.hexdigest()}; account_num: {account_num}; text: {text}; date: {date}; valutadate: {valutadate}; amount: {amount}; currency: {currency}")

            print(f"Total Rows: {count + 1}")
"""
