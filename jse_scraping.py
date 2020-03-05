# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:27:13 2020

@author: econo
"""

import requests
from bs4 import BeautifulSoup
import csv
import smtplib
import re

csv_file = open('jse_scrape.csv','w')
csv_writer =csv.writer(csv_file)
csv_writer.writerow(['Title','Summary','Date','Link'])
url= 'https://www.jamstockex.com/news/'
headers= {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

for index,jse_page in enumerate(soup.findAll('article'), start = 1):
            summary = jse_page.find('div', class_='entry-content')
            story= summary.p.text
            title= jse_page.h1.a.text
            date= jse_page.p.text
            link= jse_page.find('a')['href']
            Co = jse_page.find( text = re.compile ('JSE'))
            print(index,title)
            print(story)
            print(date)
            print(link)
            print()
            csv_writer.writerow([title,story,date,link])

csv_file.close()