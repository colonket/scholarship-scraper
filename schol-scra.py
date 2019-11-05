#!/usr/bin/env python3

"""
Created: 04-November-2019 10:00 PM
Written: by colonEndBracket :]
Description:
    This file is a rewrite of the original sou.py. For future reference,
sou.py has been left in a functional state, however, sou.py is a mess of
spaghetti code so all future efforts will be placed into this script.

To install requirements: pip install requirements.txt
"""
"""
Strategy:
1.  Get from user a url and any filters or modifiers to apply
2.  From a given link:
    2.1  search for a table called "scholarshiplistdirectory"
        2.1.1   because link elements inside this directory are for scholarships,
                store these scholarship links in the list 'scholarships'
    2.2 search for any other links on the webpage
        2.2.1   if the link hasn't been found before, open it and repeat step 1
3.  after completing the list 'scholarships' apply any filter (such as
    GPA requirements) to narrow down the list
4.  generate a csv file of scholarship information from 'scholarships'  
"""

import requests                 #request webpages
from bs4 import BeautifulSoup   #BeautifulSoup4 - Webscraping Module
import csv                      #generate csv's of scholarships
import datetime                 #timestamps for scraping
import sys                      #getting input from user


#TEMPORARY - 1. Handle User Input
#Currently just takes the url and nothing else
#Will take filters and modifiers in future
if len(sys.argv) < 2:
    print("scholarship-scraper: Not enough arguments")
    print("Usage: schol-scra.py [url]")
    exit()
elif len(sys.argv) > 2:
    print("scholarship-scraper: Too many arguments")
    print("Usage: schol-scra.py [url]")
    exit()

#2. Search link
target_url = sys.argv[1]
pullFromSLD(target_url)
#3. Apply filters and modifiers

#4. Generate CSV

#################
### FUNCTIONS ###
#################

#Called to pull scholarships from scholarshiplistdirectory
def pullFromSLD(url): 
    global scholarships
    schol_count = 0
    page = requests.get(url)
    if page.status_code != 200:
        print("could not reach {}".format(url))
        continue 
    rawhtml = BeautifulSoup(page.text, "lxml")
    for scholdir in rawhtml.find_all('table', attrs={'class:','scholarshiplistdirectory'}):
        link = scholdir.find_all("a")
        scholarships.append(link)