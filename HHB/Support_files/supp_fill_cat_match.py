# Let you fill the table categories_match with data you would like

# To Do
# 1) connect sqlite3
# 2) let the user enter searchword and category it should match show him the possible categories with numbers
# 3) write into table
# 4) close connection

import sqlite3

if __name__ == '__main__':
    # Create connection to database and tables
    conn = sqlite3.connect('HHB/Database/datadb.sqlite')
    cur = conn.cursor()

    cat_match_word = input("Please enter a Searchword, you would like to add to the database\n")

    cur.execute('''SELECT id, name FROM Category_In_Out_Supp''')
    for each in cur.fetchall():
        print(each)

    cat_match = input("Choose a catagory from above by entering the number\n")

    cur.execute('''INSERT OR IGNORE INTO Categories_Match (name, category_in_out_id)
        VALUES (?, ?)''', (cat_match_word, cat_match) )


    conn.commit()