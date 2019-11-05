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

import requests #Makes requests for pages
from bs4 import BeautifulSoup #The scraping library we will be using
import csv #Helps us generate csv's from our data
import datetime #Timestamps (yet to be implented)