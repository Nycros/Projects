# Is a support file for filling all the tables with the neccessary information like bank names, currencys, asset classes , ....

"""
To Do:
1) Fill tabels which will support the readout
"""

import sqlite3

# Create connection to database and tables
conn = sqlite3.connect('HHB/Database/datadb.sqlite')
cur = conn.cursor()

cur.executescript('''
INSERT OR IGNORE INTO Banks_Supp (name)
VALUES 
('Allianz'),
('Bawag'),
('Binance'),
('Bitpanda'),
('Bondora'),
('Cashbestand'),
('Coinbase'),
('Consorsbank'),
('Crypto.com'),
('Flatex'),
('HDI'),
('Huobi'),
('Ing. DiBa'),
('Ledger'),
('Mintos'),
('N26'),
('NÖV'),
('Paypal'),
('Privat'),
('Raika'),
('Uniqa'),
('Volksbank'),
('Wüstenrot');

INSERT OR IGNORE INTO Currency_Supp (name)
VALUES 
('EUR'),
('USD');

INSERT OR IGNORE INTO Asset_Class_Supp (name)
VALUES 
('Abfertigung'),
('Aktien/ Fonds'),
('Konto'),
('Kredit'),
('Krypto'),
('P2P'),
('Rohstoffe'),
('Sparbuch'),
('Unternehmen'),
('Versicherung');

INSERT OR IGNORE INTO Internal_or_External_Supp (int_or_ext)
VALUES 
('Internal'),
('External');

INSERT OR IGNORE INTO I_O_Supp (i_o)
VALUES 
('In'),
('Out');

''')

conn.commit()