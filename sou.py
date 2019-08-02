#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import os

base_url = 'https://www.scholarships.com'
directory_url = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory"

#Crawl the website
targets = [base_url]
scraped = []

def findTargets(url):
    global targets
    page = requests.get(url)
    rawhtml = BeautifulSoup(page.text, "lxml")
    for ul in rawhtml.find_all('ul'):
         print("Found a ul!")
         for li in ul.find_all('li'):
            try:
                timesUnknown = 0
                a = li.find('a')
                link = base_url+a['href']
                for hit in targets:
                    if( link != hit):
                        timesUnknown += 1
                    if timesUnknown == len(targets):
                        targets.append(link)
            except TypeError as e:
                     pass
    scraped.append(url)
    print(url+" crawled!")

    targets = [i for i in targets if i.startswith(directory_url)]
    
    #targets = list(dict.fromkeys(targets))



def scrapeInfo(url):
    print("Scraping from {}".format(url))
    sList = ['bluh']
    page = requests.get(url)
    rawhtml = BeautifulSoup(page.text, "lxml")

    #Get list of Scholarship Titles (scholtitle)
    titles = []
    for ele in rawhtml.select('td.scholtitle'):
        titles.append(ele.text)
    #Get list of Scholarship Amounts (scholamt)
    amounts = []
    for ele in rawhtml.select('td.scholamt'):
        amounts.append(ele.text)
    #Get list of Scholarship Due Dates (scholdd)
    duedates = []
    for ele in rawhtml.select('td.scholdd'):
        duedates.append(ele.text)

    #Print list of scholarship information as long as information is consistent
    consistent = (len(titles) == len(amounts)) and (len(amounts)==len(duedates)) 
    if( consistent ):
        for i in range(len(titles)):
            schol = "{} - {} - {}".format(titles[i],amounts[i],duedates[i])
            print(schol)
            '''
            for item in sList:
                already = False
                if(item == schol):
                    already = True
                if already == False:
                    sList.append(schol)
            '''
    else:
        print("Error Encountered: Inconsistent quantity of scholarship titles, amounts, and due dates.")


findTargets(directory_url)
for url in targets:
    scrapeInfo(url)
