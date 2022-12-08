# Is a support file for creating the databases

import sqlite3

if __name__ == "__main__":
    # Explaination on tables:
    """
    TABLE Banks: list all the banks by name
    TABLE Currency: list differen currencies by name
    TABLE Asset_Class:lists all the asset classes by Name
    TABLE Internal_or_External: a table if the expense is internal (to a account from Banks) or if it is an external to someone elses expense
    TABLE I_O: a list if the amoutn is in or otgoing
    TABLE Category_In_Out: lists all the possible categories
    TABLE Accounts: lists all the accounts
    TABLE Transaction_Text: lists all the transaction texts
    TABLE Transactions: list all transactions
    TABLE Categories_Match: list all searchwords to match the category
    """

    # Create connection to database and tables
    conn = sqlite3.connect('HHB/Database/datadb.sqlite')
    cur = conn.cursor()

    # Create tables in the database
    cur.executescript('''
    DROP TABLE IF EXISTS Banks_Supp;
    DROP TABLE IF EXISTS Currency_Supp;
    DROP TABLE IF EXISTS Asset_Class_Supp;
    DROP TABLE IF EXISTS Internal_or_External_Supp;
    DROP TABLE IF EXISTS I_O_Supp;
    DROP TABLE IF EXISTS Category_In_Out_Supp;
    DROP TABLE IF EXISTS Categories_Match;
    DROP TABLE IF EXISTS Accounts_Supp;
    DROP TABLE IF EXISTS Transaction_Text;
    DROP TABLE IF EXISTS Transactions;

    CREATE TABLE Banks_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT VARCHAR(255) UNIQUE
    );

    CREATE TABLE Currency_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT VARCHAR(255) UNIQUE
    );

    CREATE TABLE Asset_Class_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT VARCHAR(255) UNIQUE
    );

    CREATE TABLE Internal_or_External_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        int_or_ext TEXT VARCHAR(255) UNIQUE
    );

    CREATE TABLE I_O_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        i_o TEXT VARCHAR(255) UNIQUE
    );

    CREATE TABLE Category_In_Out_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT VARCHAR(255) UNIQUE,
        i_o_id INTEGER,
        FOREIGN KEY (i_o_id) REFERENCES I_O_Supp(id)
    );

    CREATE TABLE Categories_Match (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT VARCHAR(255) UNIQUE,
        category_in_out_id INTEGER,
        FOREIGN KEY (category_in_out_id) REFERENCES Category_In_Out_Supp(id)
    );

    CREATE TABLE Accounts_Supp (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT VARCHAR(255) UNIQUE,
        account_number TEXT VARCHAR(255) UNIQUE,
        bank_id INTEGER,
        asset_class_id INTEGER,
        FOREIGN KEY (bank_id) REFERENCES Banks_Supp(id),
        FOREIGN KEY (asset_class_id) REFERENCES Asset_Class_Supp(id)
    );

    CREATE TABLE Transaction_Text (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        transaction_text TEXT VARCHAR(255) UNIQUE
    );

    CREATE TABLE Transactions (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        hash TEXT VARCHAR(255) UNIQUE,
        valutadate DATETIME,
        amount FLOAT,
        transaction_text_id INTEGER,
        account_id INTEGER,
        asset_class_id INTEGER,
        category_in_out_id INTEGER,
        currency_id INTEGER,
        int_or_ext_id INTEGER,
        remarks TEXT VARCHAR(255),
        FOREIGN KEY (transaction_text_id) REFERENCES Transaction_Text(id),
        FOREIGN KEY (account_id) REFERENCES Accounts_Supp(id),
        FOREIGN KEY (asset_class_id) REFERENCES Asset_Class_Supp(id),
        FOREIGN KEY (category_in_out_id) REFERENCES Category_In_Out_Supp(id),
        FOREIGN KEY (currency_id) REFERENCES Currency_Supp(id),
        FOREIGN KEY (int_or_ext_id) REFERENCES Internal_or_External_Supp(id)
    );
    ''')

    conn.commit()