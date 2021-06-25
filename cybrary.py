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


def gg(mail):
    # open Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("/home/panda/Downloads/tel/pyCybAccCreate/chromedriver", chrome_options=chrome_options)

    def getPass():
        # generates a password for the cybrary account
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(18, 18)
        return ''.join(random.choice(chars) for x in range(size))

    # Open URL

    driver.get("https://www.cybrary.it/")

    class credentials:
        def __init__(self, password, email):
            self.password = password
            self.email = email

    creds = credentials(getPass(), mail)

    with open("account_list.txt", "a") as foo:
        foo.write("cybrary account: \n" + creds.email + "\n"
                  + "\n"+creds.password + "\n" +
                  "\n" + "----------------------------------------------------------------- "+"\n")
    time.sleep(2)

    #ok so the reaseon i think im really smart for this is because it clicks submit before the reCapcha loads
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



API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)




def funCyb():
    newMail = f"{API}?login={generateUserName()}&domain={domain}"
    reqMail = requests.get(newMail)
    mail = f"{extract(newMail)[0]}@{extract(newMail)[1]}"
    g = gg(mail)
    while True:
        time.sleep(3)
        checkMails(newMail, API=API)
        print("mail is done")

        return g

