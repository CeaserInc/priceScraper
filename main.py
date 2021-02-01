import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

URLS = ['https://www.amazon.com/GFV22CB-Ultra-Compact-G-Sync-Compatible-FreeSync-Zero-Tolerance/dp/B082DNTXJ6/']

dream_price = [1700,80]
from_email = 'ytgbgaming@gmail.com'
to_email = 'ytgbgaming@gmail.com'
from_password = "081208Ab$"
minutes = 5 #every how many minutes have to check the prices

def check_price():
    for i in range(len(URLS)):
        page = requests.get(URLS[i],headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text()
        price = soup.find(id="priceblock_ourprice").get_text()
        commaindex = price.index(',')
        converted_price = int(float(price[0:commaindex]))
        if(converted_price < dream_price[i]):
            send_mail(title,price[0:commaindex],i)
    
def send_mail(title,price,i):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    
    server.starttls()
    server.ehlo()
    
    server.login(from_email, from_password)
    
    subject = 'PRICE FELL DOWN!'
    body = title.strip() + '\n' + price + " dollars" + '\nCheck the amazon link below!\n' + URLS[i]
    
    msg = f"Subject: {subject} \n\n{body}"
    
    server.sendmail(from_email,to_email,msg)
    print("EMAIL SENT!")
    
    server.quit()
    
while(True):
    check_price()
    time.sleep(60*minutes)
