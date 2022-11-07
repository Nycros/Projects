import os

import data_readout as dr

# 01_data_readout
# 02_match_category
# 03_write_database


"""
# To Do
1) finish data readout
2) finish supp_fill_database_tables.py
3) create and finish delete none supporting database
4) finish write database
5) Create basic bar chart per category
"""
# Main Function
def main():
    # create a list of files in the folder for csv Readout
    folder = "HHB/Bank_statements"
    all_files = os.listdir(folder)

    # Read data from all csv fiels one after another
    for file in all_files:
        # Concatenating the file name with the folder
        acc_file = folder + "/" + file
        print(dr.read_file(acc_file))

# Run the main function
if __name__ == '__main__':
    main()
