#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json

#url = 'https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory'
url = 'https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/academic-major/cybersecurity'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

title_list = soup.find("table")

title_list_items = title_list.find_all(class_='scholtitle')

'''
<tr>
<td class="scholtitle"><a href="/financial-aid/college-scholarships/scholarship-directory/acad
emic-major/cybersecurity/isc²-undergraduate-cybersecurity-scholarship">(ISC)² Undergraduate Cy
bersecurity Scholarship</a></td>
<td class="scholamt">$5,000 </td>
<td class="scholdd">03/01/2020</td>
'''

for title in title_list_items:
   names = title.contents[0]
   print(names)


