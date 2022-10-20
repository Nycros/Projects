import os

import data_readout as dr

# 01_data_readout
# 02_match_category
# 03_write_database


# Main Function
def main():
    # create a list of files in the folder
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
