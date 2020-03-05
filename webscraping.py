# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:45:01 2020

@author: econo
"""

#First web scraping
import requests 
from bs4 import BeautifulSoup
import smtplib
import time

#site we are interested in

URL= 'https://www.microsoft.com/en-jm/p/halo-the-master-chief-collection/9ntm9hxnlszx?cid=msft_web_collection&activetab=pivot:overviewtab'
#the above gives information about the url link, info from where the data is being extracted

#Information about our computer
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id ="DynamicHeading_productTitle").get_text()
    price = soup.find(id = "ProductPrice_productPrice_PriceContainer").get_text()
    converted_price = float(price[4:9])

    if(converted_price<44):
        send_mail()

    print(title, price)
    print(converted_price)

def send_mail():
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('alexanthonywilliams@gmail.com','lzudiadsxljbqzkt')
    
    subject = 'Get Halo'
    body = 'Check Xbox link https://www.microsoft.com/en-jm/p/halo-the-master-chief-collection/9ntm9hxnlszx?cid=msft_web_collection&activetab=pivot:overviewtab'
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('alexanthonywilliams@gmail.com','economics4life@outlook.com', msg)
    print("Email sent")
    server.quit()
    
while(True):
    check_price()
    time.sleep()