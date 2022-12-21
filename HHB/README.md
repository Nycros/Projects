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
- The folder __Bank_statement__ contains all the csv files of my bank accounts
- The folder __Database__ contains exactly this, the SQL-database
- __Support_files__ holds all the files for creating the SQL tables and for filling them with base data
- The overall folder contains the main file and files for calculating and plotting graphs

In the next section, i will explain more in detail, what each file is for.

### Explaination of each file

TRied different plot styles
Experimented with different plots

### Problems i had during building this project
SQL write and read take long
df creation for each plot
unsure how to handle the data readout and how to update correct for time saving
not have found the right library for creating an interactive dashboard

### Further plans for this file