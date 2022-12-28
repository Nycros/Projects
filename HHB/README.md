# Budget Book
#### Video Demo:  <https://youtu.be/VmX8xf-D24Y>
#### Description:

<!--
Preview: CTRL+Shift+V
Link to Documentation for Markdown: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Your README.md file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them. Ensure you allocate sufficient time and energy to writing a README.md that documents your project thoroughly. Be proud of it! If it is too short, the system will reject it.
-->

### What is the project for?
I built this project to get an overview and control of my finance.  
1. The main function is that it reads data from different csv files and plots graphs for better understanding of the account statements.
2. Beside that, it creates an SQL database, creates tables and fills them.
3. Then the data is pulled from the database and gets prepared for data analysis.
4. At the end the prepared data will be plotted on different charts.

### Why have I decided for this project
Since several years I have, maybe as several people, an excel file for keeping track of my financial live.  
This file grew increasingly in the last years and is now a kind of monster for each single aspect of my finances.  
While the file grew increasingly, it also took me more time to maintain it.  
As I then started my coding journey, the first I thought of was to automate some of the tasks filling my excel file.  
This would save me hours and hours filling the file and maintaining it.  
Therefore, I started working on at least automating the readout of the csv files from my bank statements.  
And overall, my excel file should be replaced completely.

### Structure of the project
The project is split into several folders and files.  
- The folder __Bank_statement__ contains all the csv files of my bank accounts here I have nothing coded; it is just the files I downloaded
- The folder __Database__ contains exactly this, the SQL-database for creation of the database see the files in the __Support_files__ folder
- __Support_files__ holds all the files for creating the SQL tables and for filling them with base data
- The overall folder contains the main file and files for calculating and plotting graphs

In the next section, I will explain more in detail what each file is for.

### Explanation of each file
The first four files, I will explain, are supporting files.  
What I mean by that is, they do not need to be run every time.  
They create database tables or fill them with standard data.
#### supp_create_database_tables.py
This file will create all the database tables initially.  
I created in total ten different tables to store all the data for my budget overview.  
In the following I list all the tables and what they are used for.  
- TABLE Banks_Supp: list all the banks by name
- TABLE Currency_Supp: list different currencies
- TABLE Asset_Class_Supp: lists all the asset classes
- TABLE Internal_or_External_Supp: a table if the expense is internal (to an account from Banks) or if it is an external to someone else’s expense
- TABLE I_O_Supp: a list if the amount is in or outgoing
- TABLE Category_In_Out_Supp: lists all the possible categories
- TABLE Accounts_Supp: lists all the accounts
- TABLE Transaction_Text: lists all the transaction texts
- TABLE Transactions: list all transactions
- TABLE Categories_Match: list all search-words to match the category
#### supp_del_none_supp_tables.py
I use this file to reset the csv readout.  
So, if I start the main program and face any problems later, I need to also reset the database tables.  
Therefore, I created this file, so only the data in the tables which will be filled by the data readout of the csv files, will be deleted.  
In that way, I do not have to start from nothing again.
#### supp_fill_cat_match.py
If this code is run, it lets you enter a category name and also a search word to match both in the table "Categories_Match".  
This is needed, to match the transaction text from the account statements to a category.  
For example, let us say in the Transaction text it says something like "grocery store" and I would like to match it to the category "food and consumer goods".  
In this case, I start the program, I get asked to enter a Search word. I that case, the search word would be "grocery store".  
I then get a list of all pre-defined categories and I can choose which category I would like to match the search word.  
The search word and the category index number will then be written into the table "Categories_Match" in the database.
#### supp_fill_database_tables.py
This file is going to fill all the non-changeable data in some tables.  
Like Bank names, Currencies, categories and some others.  
I created this file for the case if I lose the tables somewhere in the future.  
In that case, I can run this program and I do not have to enter all the data manually again.
#### 00_main.py
This file is, as the name says, the main file.  
Which means, that I run this file whenever I need to read new data from a csv file from the bank.  
In combination with the files __match_category__, __write_database__ and __data_readout__. This files fills the database with all necessary data.  
This file reads all the file names from a folder and hands it over one after one to the file __write_database__.
#### write_database.py
This file now takes all the data in each single csv file.  
Creates a pandas data frame for storing the data.  
Finally, it takes all the data in the data frame and writes it via and MySQL statement into the database.  
It also updates the older entries.  
The pandas data frame is created via the file __data_readout__.
#### data_readout.py
This file now takes the data out of the csv file, transforms it and connects it with data from SQL tables and writes it into the data frame row by row.  
Afterwards it returns the whole data frame to the file __write_database__.  
The main part of this file is to match a specific category to the transaction text.  
Therefore, I have created another file called __match_category__.
#### match_catagory.py
This file pulled all the data from the category table and checks each category match text and tries to find in the transaction text.  
If it is found, it writes the category id number into the database table.  
With this file reached, all the data is handed over to the __write_database__ file and all the processed data is written into the database table.
#### 01_plot_data.py
This is the last and in parallel the most visual file. 
I decided to create a separate file independent from my main file, so I do not have to read all the csv files again and again.   
Here I write different SQL queries into different data frames.  
The data is also combined and transformed as needed.  
At the end, all the data is plotted on different graphs, to get a deeper inside into the data.  

Here I tried different plot styles and types and to be honest, I am not 100% happy with my choice.  
In the future I will try to rebuild this to make a better visual experience for the user.  
More about my problems and struggles can be read in the next paragraph.
### Problems I had during building this project
At the moment, the biggest problem I see is the processing time of this project.  
Just a few lines of csv data take exceptionally long for readout and data processing.  
But at the moment I am not sure how to handle the data readout and how to update correctly for time saving.  
Also, the file __match_category__ is terribly slow as this is a loop within a loop and therefore very slow.  

I am also struggling as said with the UI. In the future I am looking for a more interactive library for a nice User Dashboard.  
I am also thinking of transforming everything into a Flask or Django application so I can make use of CSS and HMTL and I could also access everything not only from home.  
But that is just my plan for the distant future.  

Overall, I am very proud of my solution so far and I am confident of reaching my future goals.  
### Further plans for this file
What have I planned in my next versions of my project.  
First of all, I would like to increase the speed of my project, so it is more user-friendly.  
In the next step I will try to finish all functionality and data analysis.  
Integrate a crypto tracker.   
Also, I would like to make a better UI and create a User Dashboard.  
Then transform everything into an online application using Flask or Django.  
And as a final state (if this is possible) I would like to get all the data from the banks via API connection.  
So, I am fairly sure, I have enough to do for the next months and years.  

I hope you enjoyed my description.
If you have any feedback or questions regarding my project, just contact me via https://github.com/Nycros or via email: michael.oefferl@hotmail.de.