import smtplib
import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from email.message import EmailMessage
from datetime import date
from decimal import Decimal

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "<enter email address>"
    msg['from'] = user
#########################################
#You cannot use normal password for this due to gmail restrictions#
#To generate the password below - go to https://myaccount.google.com > Security Tab > Turn on 2FA > go Back to Security tab#
#A new field should appear under 2FA called "App Passwords". Click there > Sign in again > Generate a new password (I chose Other(custom))#
#Record the key that is provided#
########################################
    password = "<enter App Password here>"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit

if __name__ == '__main__':
    milestone = <ENTER INTEGER or DECIMAL YOU WANT TO ACHIEVE>
    url = Request("https://www.google.com/finance/quote/NDQ:ASX", headers={'User-Agent': 'Mozilla/5.0'})
    html_text = urlopen(url).read()
    page_soup = soup(html_text, "html.parser")
    getmoneys = page_soup.findAll("div",{"class":"YMlKec fxKbKc"})
    NDQ_current = getmoneys[0].text
    dollars_dec = Decimal(NDQ_current.strip('$'))
    if dollars_dec > milestone:
        print(dollars_dec)
        email_alert("Stock is BOOMING!", "The milestone has been reached. NDQ has crossed $50.00 per share!", "<email dest 1>, <email dest 2>")
    else:
        email_alert("Stock has not boomed yet :( ", "The price at this point in time is: " + NDQ_current, "<email dest 1>, <email dest 2>")
        
#THE ENTIRE SCRIPT IS GENERATED THROUGH CRONTAB ON MAC. 
#Feel free to send a message to get a better understanding on how this is done.
