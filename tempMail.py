import os
import random
import re
import string
import sys
import requests

def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def extract(newMail):
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

def getEmailName():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(3, 3)
  return ''.join(random.choice(chars) for x in range(size))
# Got this from https://stackoverflow.com/a/43952192/13276219
def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def deleteMail(mail, newMail, requests=None):
    url = 'https://www.1secmail.com/mailbox'
    data = {
        'action': 'deleteMailbox',
        'login': f'{extract(newMail)[0]}',
        'domain': f'{extract(newMail)[1]}'
    }

    print_statusline("Disposing your email address - " + mail + '\n')
    req = requests.post(url, data=data)

def checkMails(newMail, API):
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