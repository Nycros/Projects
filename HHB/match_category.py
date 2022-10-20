# matches a category to the text

import sqlite3

def match_category(text):
    # Create connection to database and tables
    conn = sqlite3.connect('HHB/datadb.sqlite')
    cur = conn.cursor()

    # select all elements in name column
    cur.execute("SELECT name FROM Categories_Match")

    # fetch all the matching rows
    all_cat = cur.fetchall()

    # print(all_cat)    # Printout for debug

    # Readout the category which matches the text
    for category in all_cat:
        # print(category[0])    # Print each row of the selected column
        if category[0] in text:
            cur.execute("SELECT category_in_out_id FROM Categories_Match WHERE name = ?", category)
            cat_id = cur.fetchone()[0]
            # correct_cat = category[0]
            # print(f"Category: {category[0]}; ID: {id}")   # Printout for debug
            break
        else:
            cat_id = None
            # correct_cat = None
    
    return cat_id

