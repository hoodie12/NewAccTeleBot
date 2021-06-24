# Import Module

import time
import string
import random
import requests
import sys
import re
import os
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import telebot

API_token = "1802551249:AAGz3zVXxI5qzBwTzDD3CHyZQHK-Fegio7Q"
bot = telebot.TeleBot(API_token)


def AAS(message):
  if message == "testme":
    print("print hh")
    return False
  else:
    return True

@bot.message_handler(func=AAS)
def send_price(message):
    import smtplib
    from email.mime.text import MIMEText
    print("i started")
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = 'between6and30taken@gmail.com'
    password = 's5Lzd6d22oA4'
    sender = 'between6and30taken@gmail.com'
    targets = ['iamhoodie12@gmail.com']

    msg = MIMEText("A new account has been created with the service")
    msg['Subject'] = 'Hello'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()

    e = everything()
    msg = (e[0] + "\n" + e[1])
    print("this is msg " +msg)
    bot.send_message(message.chat.id, msg)


def getEmailName():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(3, 3)
  return ''.join(random.choice(chars) for x in range(size))

API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def extract(newMail):
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

# Got this from https://stackoverflow.com/a/43952192/13276219
def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def deleteMail(mail, newMail):
    url = 'https://www.1secmail.com/mailbox'
    data = {
        'action': 'deleteMailbox',
        'login': f'{extract(newMail)[0]}',
        'domain': f'{extract(newMail)[1]}'
    }

    print_statusline("Disposing your email address - " + mail + '\n')
    req = requests.post(url, data=data)

def checkMails(newMail):
    print("Checkmail started")
    reqLink = f'{API}?action=getMessages&login={extract(newMail)[0]}&domain={extract(newMail)[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        print_statusline("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
    else:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        x = 'mails' if length > 1 else 'mail'
        print_statusline(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)")

        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'All Mails')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract(newMail)[0]}&domain={extract(newMail)[1]}&id={i}'
            req = requests.get(msgRead).json()
            rip = req["htmlBody"]
            urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', rip)
            for u in urls:
                index = u.find("verify")
                if index > 0:
                    requests.get(u)
    print("Checkmail ended")


def gg(mail):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/home/ubuntu/tel/pyCybAccCreate/chromedriver')

    def getPass():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(18, 18)
        return ''.join(random.choice(chars) for x in range(size))

    # Open URL

    driver.get("https://www.cybrary.it/")
    getEmail = mail

    class credentials:
        def __init__(self, password, email):
            self.password = password
            self.email = email

    creds = credentials(getPass(), getEmail)



    with open("account_list.txt", "a") as foo:
        foo.write("\n"+creds.password + "\n")
    with open("account_list.txt", "a") as foo:
        foo.write(creds.email + "\n")
    with open("account_list.txt" , "a") as foo:
        foo.write("\n" + "----------------------------------------------------------------- "+"\n")
    time.sleep(2)
    initEmail = driver.find_element_by_xpath(
        "/html/body/div/div[1]/div/main/div[1]/div/div/div/div/div[2]/div/div/div/form/div/input")
    initEmail.send_keys(creds.email)
    logging.info(creds.email)
    crt_button = driver.find_element_by_xpath(
        "/html/body/div/div[1]/div/main/div[1]/div/div/div/div/div[2]/div/div/div/form/button")
    crt_button.click()
    time.sleep(2)
    initPass = driver.find_element_by_xpath(
        "/html/body/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/form/div[2]/input")
    initPass.send_keys(creds.password)
    conPass = driver.find_element_by_xpath(
        "/html/body/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/form/div[4]/input")
    conPass.send_keys(creds.password)
    logging.info(creds.password)
    EULAbtn = driver.find_element_by_xpath(
        "/html/body/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/form/div[6]/div[2]/label/div/div[1]/input")
    EULAbtn.click()
    conBtn = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/form/button")
    conBtn.click()
    time.sleep(3)
    driver.quit()

    FC = [creds.password, creds.email]
    print("this is FC " + FC[0] + "\n" + FC[1])
    return FC



def everything():
    newMail = f"{API}?login={generateUserName()}&domain={domain}"
    reqMail = requests.get(newMail)
    mail = f"{extract(newMail)[0]}@{extract(newMail)[1]}"
    g = gg(mail)
    while True:
        time.sleep(3)
        checkMails(newMail)
        print("mail is done")

        return g

bot.polling()