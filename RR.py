import re
import string
import os
import random
import re
import string
import sys

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
from tempMail import extract
from tempMail import generateUserName
from tempMail import checkMails
import names

API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

def riely(mail):
    # open Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/home/panda/Downloads/tel/CybAccTeleBot/chromedriver', chrome_options=chrome_options)

    def getPass():
        # generates a password for the cybrary account
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(18, 18)
        return ''.join(random.choice(chars) for x in range(size))

    # Open URL

    driver.get("https://learning.oreilly.com/p/register/")

    class credentials:
        def __init__(self, password, email):
            self.password = password
            self.email = email

    creds = credentials((getPass()+str(1)), mail)

    with open("account_list.txt", "a") as foo:
        foo.write("O'Riely account: \n" + creds.email + "\n"
                  + "\n"+creds.password + "\n" +
                  "\n" + "----------------------------------------------------------------- "+"\n")
    time.sleep(2)

    txt_Fname = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div[2]/label/input")
    txt_Fname.send_keys(names.get_first_name())
    txt_Fname = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div[3]/label/input")
    txt_Fname.send_keys(names.get_last_name())
    #ok so the reaseon i think im really smart for this is because it clicks submit before the reCapcha loads
    txt_Email = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div[4]/label/input")
    txt_Email.send_keys(creds.email)
    logging.info(creds.email)
    txt_Pass = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div[5]/label/input")
    txt_Pass.send_keys(creds.password)
    logging.info(creds.password)
    conBtn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/button")
    conBtn.click()
    time.sleep(3)
    driver.quit()

    FC = [creds.password, creds.email]
    print("this is FC " + FC[0] + "\n" + FC[1])
    return FC

def funRiely():
    newMail = f"{API}?login={generateUserName()}&domain={domain}"
    reqMail = requests.get(newMail)
    mail = f"{extract(newMail)[0]}@{extract(newMail)[1]}"
    g = riely(mail)
    while True:
        time.sleep(3)
        checkMails(newMail, API=API)
        print("mail is done")
        print(g)
        return g

