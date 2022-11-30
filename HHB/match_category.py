# matches a category to the text

import sqlite3

def match_category(text, conn, cur):

    # select all elements in name column
    cur.execute("SELECT name FROM Categories_Match")

    # fetch all the matching rows
    all_cat = cur.fetchall()

    # print(all_cat)    # Printout for debug

    # if there are no catagories
    if not all_cat:
        return None

    """
    iterate over words of transcation text and check if it exists in all categories
    words = text.split()

    for word in words:
        if word.lower() in all_cat.lower():
            cur.execute("SELECT category_in_out_id FROM Categories_Match WHERE name = ?", word)
            cat_id = cur.fetchone()[0]
            # correct_cat = search_val[0]
            # print(f"Category: {search_val[0]}; ID: {id}")   # Printout for debug
            break
        else:
            cat_id = None
            # correct_cat = None
    """
    
    # Readout the category which matches the text
    for search_val in all_cat:
        # print(search_val[0])    # Print each row of the selected column
        if search_val[0].lower() in text.lower():
            cur.execute("SELECT category_in_out_id FROM Categories_Match WHERE name = ?", search_val)
            cat_id = cur.fetchone()[0]
            # correct_cat = search_val[0]
            # print(f"Category: {search_val[0]}; ID: {cat_id}")   # Printout for debug
            break
        else:
            cat_id = None
            # correct_cat = None
    
    return cat_id

