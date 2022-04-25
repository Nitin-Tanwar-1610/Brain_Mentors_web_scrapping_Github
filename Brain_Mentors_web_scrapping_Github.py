#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install beautifulsoup4


# In[ ]:


from bs4 import BeautifulSoup
import requests
import html5lib
import smtplib
import time


def userInput():
    global flipkartProductURL
    global amazonProductURL
    flipkartProductURL = input('Enter the flipkart product URL: ')
    amazonProductURL = input('Enter the amazon product URL: ')

def trackPrices():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    if flipkartProductURL and amazonProductURL:
        flipkartResponse = requests.get(flipkartProductURL,headers=headers)
        amazonResponse = requests.get(amazonProductURL,headers=headers)
        flipkartSoup = BeautifulSoup(flipkartResponse.content,'html5lib')
        amazonSoup = BeautifulSoup(amazonResponse.content,'html5lib')
        flipkartProductPrice = float(flipkartSoup.find('div',attrs='_30jeq3 _16Jk6d').text.replace(',','')[1:])   
        amazonProductPrice = float(amazonSoup.find('span',attrs='priceBlockDealPriceString').text.replace(',','')[1:])
        print('Flipkart product price is ',str(flipkartProductPrice))
        print('Amazon product price is ',str(amazonProductPrice))
        if flipkartProductPrice and amazonProductPrice:
            sendEmail(amazonProductPrice,flipkartProductPrice)

def sendEmail(amazonPrice,flipkartPrice):
    message = ''
    if amazonPrice and flipkartPrice and (amazonPrice > flipkartPrice):
        message = 'Flipkart price is low. Price is Rs'+ str(flipkartPrice)
    elif flipkartPrice > amazonPrice:
        message = 'Amazon price is low. price is Rs'+ str(amazonPrice)
    fromEmail = 'nitintanwar1610@gmail.com'
    toEmail = 'nitintanwar1510@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromEmail, '1234567')
    server.sendmail(fromEmail,toEmail,message)
    print('Mail sent succesfully')
    server.quit()

userInput()
while True:
    trackPrices()
    time.sleep(5)
    


# In[ ]:




