#!/usr/bin/env python3

import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['title', 'amount', 'due date', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    titles = ['hewwo']
    amounts = ['uwu']
    duedates = ['awa']
    slinks = ['babie']
    quantity = len(titles)
    for i in range(quantity):
        schol = "{} - {} - {} - {}".format(titles[i],amounts[i],duedates[i],slinks[i])
        writer.writerow({'title': titles[i],'amount': amounts[i],'due date': duedates[i],'link': slinks[i]})