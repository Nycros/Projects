# Budget Book
#### Video Demo:  <URL HERE>
#### Description:

<!--
Preview: CTRL+Shift+V
Link to Docuemntation for Markdown: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Your README.md file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them. Ensure you allocate sufficient time and energy to writing a README.md that documents your project thoroughly. Be proud of it! If it is too short, the system will reject it.
-->

### What is the project for?
I built this project to get an overview and control of my finance.  
There are several functions of this project.
1. The main function is, that it reads data from different csv files and plots graphs for better understanding of the account statements.
2. Beside that, it creates an SQL database, creates tabels and fills them.
3. Then the data is pulled from the database and gets prepared for dataanalysis.
4. At the end the prepared data will be plotted on different charts.

### Why have i decided for this project
Since several years i have, amybe as several people, an excel file for keeping track of my financial live.  
This file grew more and more in the last years and is now a kind of monster for each single aspect of my finances.  
While the file grew more and more, it also took me more and more time for maintaining it.  
As i then started my coding journey, the first i thought of, was to automate some of the tasks filling my excel file.  
This would save me hours and hours filling the file and maintaining it.  
Therefore i started working on at least autoating the readout of the csv files from my bank statements.  
And in the long run, my excel file should be replaced completely.

### Structure of the project
The project is split into several folders and files.  
- The folder __Bank_statement__ contains all the csv files of my bank accounts here i have nothing coded, it is just the files i downloaded
- The folder __Database__ contains exactly this, the SQL-database for creation of the database see the files in the __Support_files__ forlder
- __Support_files__ holds all the files for creating the SQL tables and for filling them with base data
- The overall folder contains the main file and files for calculating and plotting graphs

In the next section, i will explain more in detail, what each file is for.

### Explaination of each file
The first four files, i will explain, are supporting files.  
What i mean with that is, they not need to be run every time.  
They create database tables or fill them with standard data.
#### supp_create_database_tables.py
This file will create all the database tables initially.  
I created in total ten different tabels to store all the data for my budget overview.  
In the following i list all the tabels and what they are used for.  
- TABLE Banks_Supp: list all the banks by name
- TABLE Currency_Supp: list different currencies
- TABLE Asset_Class_Supp: lists all the asset classes
- TABLE Internal_or_External_Supp: a table if the expense is internal (to an account from Banks) or if it is an external to someone elses expense
- TABLE I_O_Supp: a list if the amount is in or outgoing
- TABLE Category_In_Out_Supp: lists all the possible categories
- TABLE Accounts_Supp: lists all the accounts
- TABLE Transaction_Text: lists all the transaction texts
- TABLE Transactions: list all transactions
- TABLE Categories_Match: list all searchwords to match the category
#### supp_del_none_supp_tables.py
I use this file, to lets say reset the csv readout.  
So if i start the main program and face any problems later on, i need to reset also the database tables.  
Therfore i created this file, so only the data in the tables which will be filled by the data readout of the csv files, will be deleted.  
In that way, i do not have to start from scratch again.
#### supp_fill_cat_match.py
If this code is run, it let you enter a category name and also a search word to match both in the table "Categories_Match".  
This is needed, to match the transaction text from the account statements to a category.  
For example, lets say in the Transaction text it says something like "grocery store" and i would like to match it to the category "food and consumer goods".  
In this case, i start the program, i get asked to enter a Searchword. I that case, the searhword would be "grocery store".  
I then get a list of all pre defined catgories and i can choose to which category i would like to match the searchword.  
The searchword and the category index number, will then be written into the table "Categories_Match" in the database.
#### supp_fill_database_tables.py
This file is going to fill all the non changeable data in some tables.  
Like BAnk names, Curencies, catagories and some other.  
I created this file for the case, if i loose the tables somewhere in the future.  
In that case, i can run this program and i do not have to enter all the data manually again.
#### 00_main.py
#### match_catagory.py
#### write_database.py
#### data_readout.py
#### 01_plot_data.py

TRied different plot styles
Experimented with different plots

### Problems i had during building this project
SQL write and read take long
df creation for each plot
unsure how to handle the data readout and how to update correct for time saving
not have found the right library for creating an interactive dashboard

### Further plans for this file