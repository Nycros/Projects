import csv

"""
# needed steps:
1) add header
2) read data
3) check if all rows are equal in length
4) transform data
    account num
    text
    date    --> date
    date    --> date
    amount  --> float
    currency
5) write data into database
"""

"""
For next time: Problem is, if i use the dict reader, i only read from the second line, as the first one is recognized as header.
Possible solutions:
1) add header to the csv file: 
    https://stackoverflow.com/questions/50701023/insert-new-line-in-csv-at-second-row-via-python
    https://www.geeksforgeeks.org/how-to-add-a-header-to-a-csv-file-in-python/#:~:text=A%20header%20of%20the%20CSV,back%20into%20the%20CSV%20file.
2) read the header also: 
    https://www.tutorialspoint.com/python-read-csv-file-with-pandas-without-header#:~:text=To%20read%20CSV%20file%20without,in%20the%20read_csv()%20method.
"""

# Read data from csv
acc_file = ('HHB/PSK.csv')
with open(acc_file, 'r') as fhandle:
    csv_reader = csv.DictReader(fhandle, delimiter=';', fieldnames=['account_num', 'text', 'date', 'valutadate', 'amount', 'currency'])
    header = next(csv_reader)

    print(type(csv_reader))

    print(header)

    # loop over data and print it
    tot_amount = 0
    for count, row in enumerate(csv_reader):
        # printout for debug
        # for i, value in enumerate(row):
        #     print(f"row {count} : {i}th value :{value}", end = '\n')
        tot_amount += float(row['amount'].replace(',','.'))
        print(row['amount'])
        if count > 10:
            break
    
print(tot_amount)
