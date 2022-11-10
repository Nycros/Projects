import os
import sqlite3

import write_database as wd

"""
# To Do
1) finish data readout
2) Done: finish supp_fill_database_tables.py
3) Done: create and finish delete none supporting database
4) Done: finish fill catagories match program
4) Done: finish write database
5) Create basic bar chart per category
"""
# Main Function
def main():
    # Create connection to database and tables
    conn = sqlite3.connect('HHB/Database/datadb.sqlite')
    cur = conn.cursor()

    # create a list of files in the folder for csv Readout
    folder = "HHB/Bank_statements"
    all_files = os.listdir(folder)

    # Read data from all csv fiels one after another
    for file in all_files:
        # Concatenating the file name with the folder
        acc_file = folder + "/" + file
        wd.write_datab(acc_file, conn, cur)

    conn.commit()

# Run the main function
if __name__ == '__main__':
    main()
