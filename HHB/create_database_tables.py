import sqlite3

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
DROP TABLE IF EXISTS Catagory_In_Out;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS Transaction_Text;
DROP TABLE IF EXISTS Transactions;

CREATE TABLE Banks (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Currency (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Asset_Class (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Internal_or_External (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    int_or_ext TEXT UNIQUE
);

CREATE TABLE I_O (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    i_o TEXT UNIQUE
);

CREATE TABLE Catagory_In_Out (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    i_o_id INTEGER,
    asset_class_id INTEGER
);

CREATE TABLE Accounts (
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
    catagory_in_out_id INTEGER,
    currency_id INTEGER,
    int_or_ext_id INTEGER,
    remarks Text
);
''')