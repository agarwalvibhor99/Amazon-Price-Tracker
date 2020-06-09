import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Apple-Watch-GPS-40mm-Aluminum/dp/B07XR5TRSZ/ref=sr_1_4?dchild=1&keywords=apple+watch&qid=1591688861&sr=8-4'

headers = {#Put Your User Agent Here}

def price_check():
    page = requests.get(URL, headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    title = title.strip()
    print(title)
    price = float(price.split("$")[1])
    print(price)

    if(price<250):
        send_email(title, price)


def send_email(title, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('youremailid@domain', 'password')

    subject = "Amazon Price Drop Alert"
    body = "Price for {} fell down! New price is $ {} \nCheck the link https://www.amazon.com/Apple-Watch-GPS-40mm-Aluminum/dp/B07XR5TRSZ/ref=sr_1_4?dchild=1&keywords=apple+watch&qid=1591688861&sr=8-4".format(title, price)

    msg = f"Subject: {subject}\n{body}"
    
    server.sendmail(
        'from email id',
        'to email id',
        msg
    )
    print("Email successfully sent")
    server.quit()


price_check()