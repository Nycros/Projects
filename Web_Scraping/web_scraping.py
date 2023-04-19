""" This file will scrape Name and Phone number from inernet from a phone book page"""

import requests
from bs4 import BeautifulSoup
import csv
data=[]
obj={}

"""
replace  umlaute
find more data (500)
"""


# Storing the data in an list of dicts
for name in ['Alois', 'Anna', 'Alfred', 
             'Berta', 
             'Carina', 
             'Elias', 'Ella', 'Emilia', 'Emma', 'Erika', 'Ernst', 'Erwin', 
             'Fabian', 'Franz', 'Felix', 'Friedrich', 
             'Gustav', 'Günther', 'Gerti', 
             'Hannah', 'Hans', 'Harald', 
             'Jakob', 'Jan', 'Jasmin', 'Johanna', 'Jonas', 'Josef', 'Julia',
             'Kevin', 'Kerstin',
             'Lea', 'Lena', 'Leon', 'Lukas', 'Leoppold',
             'Manuela', 'Manual', 'Maria', 'Marie', 'Martin', 'Mathias', 'Matteo', 'Mia', 'Michael',
             'Noah',
             'Otto', 'Oliver',
             'Paul', 'Peter', 'Petra',
             'Regina', 'Roland',
             'Sabrina', 'Sarah', 'Sebastian', 'Stefan',
             'Tamara', 'Thomas', 'Theo',
             'Walter', 'Wilfried']:
    for page in range(1,6):
        target_website = "https://www.11880.com/suche/" + name + "/muenchen?source=tb24&utm_source=tb24&personen=1&modul=direct&page=" + str(page)

        # target_website = "https://www.11880.com/suche/hans/muenchen?source=tb24&utm_source=tb24&personen=1&modul=direct&page=3"
        resp = requests.get(target_website)
        soup=BeautifulSoup(resp.text, 'html.parser')
        allResults = soup.find_all("li",{"class":"result-list-entry result-list-entry--clickable result-list-entry--hoverable search-result-list-item search-result-entry-item"})
        # print(allResults)
        # print(len(allResults[0]))
        for i in range(0,len(allResults)):
            try:
                obj["name"]=allResults[i].find("h2",{"class":"result-list-entry-title__headline result-list-entry-title__headline--ellipsis"}).text.strip()
            except:
                obj["name"]=None
            try:
                obj["phoneNumber"]=allResults[i].find("span",{"class":"result-list-entry-phone-number__label"}).text.strip().replace(u"\xa0", "-")
            except:
                obj["phoneNumber"]=None
            # try:
            #     obj["address"]=allResults[i].find("div",{"class":"result-list-entry-address mb-md-3"}).text.strip()
            # except:
            #     obj["address"]=None
            data.append(obj)
            obj={}
# print(data)

with open("Web_Scraping/output2.csv", "w", encoding = 'utf8', newline = '') as f:
    comp = ["GmbH", "KG", "AG"]
    for each in data:
        name = each["name"]
        if any(True for i in comp if i in name):
            continue
        number = each["phoneNumber"]
        if number == "None":
            continue
        # f.write(str(name) + " " + str(number) + "\n")
        data = [str(name), str(number)]
        a = csv.writer(f)
        a.writerow(data)


"""
# Writing the dat ainto an text file
f = open("Web_Scraping/output.txt", "a")

for name in ["Hans", "Michael", "Erika", "Martin", "Julia", "Erwin", "Josef", "Sebastian", "Manuela", "Jasmin"]:
    for page in range(1,10):
        target_website = "https://www.11880.com/suche/" + name + "/muenchen?source=tb24&utm_source=tb24&personen=1&modul=direct&page=" + str(page)

        # target_website = "https://www.11880.com/suche/hans/muenchen?source=tb24&utm_source=tb24&personen=1&modul=direct&page=3"
        resp = requests.get(target_website)
        soup=BeautifulSoup(resp.text, 'html.parser')
        allResults = soup.find_all("li",{"class":"result-list-entry result-list-entry--clickable result-list-entry--hoverable search-result-list-item search-result-entry-item"})
        # print(allResults)
        # print(len(allResults[0]))
        for i in range(0,len(allResults)):
            try:
                name = allResults[i].find("h2",{"class":"result-list-entry-title__headline result-list-entry-title__headline--ellipsis"}).text.strip()
            except:
                name = None
            try:
                number = allResults[i].find("span",{"class":"result-list-entry-phone-number__label"}).text.strip().replace(u"\xa0", "-")
            except:
                number = None
            # try:
            #     obj["address"]=allResults[i].find("div",{"class":"result-list-entry-address mb-md-3"}).text.strip()
            # except:
            #     obj["address"]=None
            f.write("Name: " + str(name) + " Number: " + str(number) + "\n")
f.close()
"""