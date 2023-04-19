import os

files = ["AT186000020610053875_main.xlsx",
"AT813293900004319257_main.xlsx",
"DE94100110012627440517_main.xlsx",
"AT246000020610053573_main.xlsx",
"AT701921080125925992_main.xlsx",
"AT206000000501250007_main.xlsx",
"AT496000000516132680_main.xlsx",
"AT796000020616034961_main.xlsx",
"31010981871_main.xlsx",
"AT231948031010981863_main.xlsx",
"1554-31192_main.xlsx",
"AT946000000516136332_main.xlsx",
"2275735_main.xlsx",
"BO165A997_main.xlsx",
"Crypto.com Debit Card_main.xlsx",
"Coinbase_main.xlsx",
"Bitpanda_main.xlsx",
"Binance_main.xlsx",
"Crypto.com_main.xlsx"
]

for file in files:
    f = open(file, "w")
    f.close()