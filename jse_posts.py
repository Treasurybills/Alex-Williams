# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:07:21 2020

@author: econo
"""

#Scraping for a text
import requests
from bs4 import BeautifulSoup
import re
import smtplib

def check_news():
    url = 'https://www.jamstockex.com/news/'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    j_news= requests.get(url, headers = headers)
    soup = BeautifulSoup(j_news.content, 'html.parser')
    jse_posts = soup.findAll( "header",{"class":"entry-header"})


    for post in jse_posts:
        link = post.find('a')['href']
        title = post.find("h1", {"class":"entry-title h4"}).get_text().replace('\n', '')
        JSE = post.find(text = re.compile ('Appoints'))
   
        if JSE!=None:
            send_mail()
            print(title, link)
def send_mail():
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('alexanthonywilliams@gmail.com','lzudiadsxljbqzkt')
    
    subject = 'JSE News'
    body = 'Check link https://www.jamstockex.com/news/  '
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('alexanthonywilliams@gmail.com','economics4life@outlook.com', msg)
    print("Email sent")
    server.quit()

check_news()
     

   

   
    