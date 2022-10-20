# Is a support file for creating the databases

import sqlite3

# Explaination on tables:
"""
TABLE Banks: list all the banks by name
TABLE Currency: list differen currencies by name
TABLE Asset_Class:lists all the asset classes by Name
TABLE Internal_or_External: a table if the expense is internal (to a account from Banks) or if it is an external to someoneelses expense
TABLE I_O: a list if the amoutn is in or otgoing
TABLE Category_In_Out: lists all the possible categories
TABLE Accounts: lists all the accounts
TABLE Transaction_Text: lists all the transaction texts
TABLE Transactions: list all transactions
TABLE Categories_Match: list all searchwords to match the category
"""

# Create connection to database and tables
conn = sqlite3.connect('HHB/datadb.sqlite')
cur = conn.cursor()

# Create tables in the database
cur.executescript('''
DROP TABLE IF EXISTS Banks;
DROP TABLE IF EXISTS Currency;
DROP TABLE IF EXISTS Asset_Class;
DROP TABLE IF EXISTS Internal_or_External;
DROP TABLE IF EXISTS I_O;
DROP TABLE IF EXISTS Category_In_Out;
DROP TABLE IF EXISTS Categories_Match;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS Transaction_Text;
DROP TABLE IF EXISTS Transactions;

CREATE TABLE Banks_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Currency_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Asset_Class_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Internal_or_External_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    int_or_ext TEXT UNIQUE
);

CREATE TABLE I_O_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    i_o TEXT UNIQUE
);

CREATE TABLE Category_In_Out_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    i_o_id INTEGER,
    asset_class_id INTEGER
);

CREATE TABLE Categories_Match (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    category_in_out_id INTEGER
);

CREATE TABLE Accounts_Supp (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    account_number TEXT UNIQUE,
    bank_id INTEGER,
    asset_class_id INTEGER
);

CREATE TABLE Transaction_Text (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    transaction_text TEXT UNIQUE
);

CREATE TABLE Transactions (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    hash INTEGER,
    valutadate DATE,
    amount INTEGER,
    transaction_text_id INTEGER,
    account_id INTEGER,
    asset_class_id INTEGER,
    category_in_out_id INTEGER,
    currency_id INTEGER,
    int_or_ext_id INTEGER,
    remarks Text
);
''')