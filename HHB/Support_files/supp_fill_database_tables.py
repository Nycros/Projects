# Is a support file for filling all the tables with the neccessary information like bank names, currencys, asset classes , ....
# All those informations, that are most likely immutable

import sqlite3

if __name__ == "__main__":
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
    ('Bank 99'),
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
    ('Out'),
    ('Both');

    INSERT OR IGNORE INTO Category_In_Out_Supp (name, i_o_id)
    VALUES
    ('Gehalt', 1),
    ('Zinsen', 1),
    ('Dividenden', 1),
    ('Steuerausgleich', 1),
    ('Unternehmen Einnahmen', 1),
    ('Sonstige', 1),
    ('P2P Kredite', 1),
    ('Kryptowährungen', 1),
    ('Sparbücher', 1),
    ('Aktien', 1),
    ('ETF-Sparplan', 1),
    ('Cashbestand', 1),
    ('Bausparer', 1),
    ('Unternehmen Ausgaben', 2),
    ('Autoversicherung NV', 2),
    ('Autoversicherung Uniqa', 2),
    ('BU-Versicherung HDI', 2),
    ('Family Card Versicherung', 2),
    ('Haushalt, Unfall, Rechtsschutz', 2),
    ('Lebensversicherung Louisa und Sebastian', 2),
    ('Lebensversicherung Uniqa', 2),
    ('Pensionsversicherung', 2),
    ('Private Krankenversicherung', 2),
    ('Haushaltsgeld', 2),
    ('Lebensmittel/ Verbrauchsgüter', 2),
    ('Haus Reperatur/ Erhaltung/ Ausstattung', 2),
    ('Hobby/ Geschenke/ Gesundheit/ Spiele', 2),
    ('Kleidung/ Frisör', 2),
    ('Handy', 2),
    ('Internet', 2),
    ('Kontoführung', 2),
    ('Alpenverein', 2),
    ('Naturfreunde', 2),
    ('ÖAMTC', 2),
    ('Rettungshundestaffel', 2),
    ('Rotes Kreuz', 2),
    ('Sportverein', 2),
    ('Kreditrückzahlung Fritz', 2),
    ('Kreditkarte', 2),
    ('Kreditrückzahlung + Lebensversicherung', 2),
    ('Reparaturen', 2),
    ('Tanken', 2),
    ('Autokauf', 2),
    ('Verkehrsstrafen', 2),
    ('Audible', 2),
    ('Keeper Abo', 2),
    ('Kletterhalle', 2),
    ('Amazon Prime', 2),
    ('NETFLIX', 2),
    ('Blizzard', 2),
    ('Spotify/ 7 Mind', 2),
    ('Google One', 2),
    ('HP Instant Ink', 2),
    ('Urlaub/ Freizeit', 2),
    ('Humankapital', 2),
    ('Sonstige Ausgaben', 2),
    ('Arzt', 2);

    INSERT OR IGNORE INTO Accounts_Supp (name, account_number, bank_id, asset_class_id)
    VALUES
    ('Vorsorgekasse', '1893161286', 1, 1),
    ('Consorsbank Depotkonto', 'Consorsbank Depotkonto', 8, 2),
    ('Consorsbank Verrechnungskonto', 'DE26760300800880640130', 8, 2),
    ('Flatex Depotkonto', '31010981871', 10, 2),
    ('Flatex Verrechnungskonto', 'AT231948031010981863', 10, 2),
    ('Raika Investkonto', 'AT813293900004319257', 20, 2),
    ('Bawag Kreditkarte', 'AT206000000501250007', 2, 4),
    ('Hausbau Kredit', 'Würo', 23, 4),
    ('Binance Konto', 'Binance', 3, 5),
    ('Bitpanda Konto', 'Bitpanda', 4, 5),
    ('Coinbase Konto', 'Coinbase', 7, 5),
    ('Huobi Konto', 'Huobi', 12, 5),
    ('Ledger', 'Ledger', 14, 5),
    ('Crypto.com Wallet', 'Crypto.com Wallet', 9, 5),
    ('Crypto.com Debit Card', 'Crypto.com Debit Card', 9, 4),
    ('Bondora Konto (aktueller Wert)', 'BO165A997', 5, 6),
    ('Mintos Konto (aktueller Wert)', '2275735', 15, 6),
    ('Edelmetalle', 'Metal', 19, 7),
    ('Bausparer', '1554-31192', 22, 8),
    ('Bawag Bildungssparbuch', 'AT946000000516136332', 2, 8),
    ('Bawag Eiserne Res.', 'AT496000000516132680', 2, 8),
    ('Bawag Gehaltskonto', 'AT186000020610053875', 2, 3),
    ('Bawag Kreditkonto', 'AT246000020610053573', 2, 3),
    ('Bawag Urlaub/ Auto/ Haus', 'AT796000020616034961', 2, 8),
    ('Ing. DiBa Fixkosten Versicherung / Handy / Internet', 'AT701921080125925992', 13, 3),
    ('Paypal Konto Privat', 'DE18120700883004792803', 18, 3),
    ('Urlaubskonto', 'DE16100110012623779589', 16, 3),
    ('Haushaltskonto', 'AT303293900004322988', 20, 3),
    ('Bar', 'Bar', 6, 3),
    ('Paypal Konto Business', 'DE13120700883009764434', 18, 9),
    ('Unternehmenskonto', 'DE94100110012627440517', 16, 9),
    ('Autoversicherung', '1.976.423/8', 17, 10),
    ('Haushaltsversicherung/ Unfall / Rechtsschutz/ Haftpflicht', '3.646.442/9', 17, 10),
    ('Kapitalversicherung Louisa und Sebastian', '5.139.878/0', 17, 10),
    ('Lebensversicherung', '30/23370034-0', 21, 10),
    ('Lebensversicherung Bawag für Kredit', '0/39/1164185', 2, 10),
    ('Pensionsversicherung NV', '5.133.015/0', 17, 10),
    ('Pensionsversicherung Uniqa', '28347590', 21, 10),
    ('BU-Versicherung', '40-19310279', 11, 10),
    ('Private Krankenversicherung', '700/1193031-3', 21, 10);


    ''')

    conn.commit()