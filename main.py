# Import Module

import time
import string
import random
import requests
import sys
import re
import os
import logging
import pyotp
from cybrary import funCyb
import telebot
from dotenv import DotEnv
import smtplib
from email.mime.text import MIMEText
from RR import funRiely

myEnv = DotEnv()
API_token = myEnv.get("API_token")
print(API_token)
bot = telebot.TeleBot(API_token)
authKey = myEnv.get("authKey")
totp = pyotp.TOTP(authKey)
print(totp.now())
def sendmail():
    print("sending email")

    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = myEnv.get("Email_sender_addr") #sender email
    password = myEnv.get("Email_sender_pwd")#sender email password
    sender = myEnv.get('Email_sender_addr') #your not that dumb are you
    targets = [myEnv.get("Email_reciver_addr")] #email reciver
#
    msg = MIMEText("A new account has been created with the service")
    msg['Subject'] = 'Hello'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)
#
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()

def AAS(message):
  otpc = message.text
  otpc = otpc.translate({ord(i):None for i in 'OCoc'}) #removes the a and c from the message
  if otpc == totp.now():
    print("otp correct")
    return True
  else:
    print("opt incorrect: " + otpc + " correct otp: " + str(totp.now()))
    return False
@bot.message_handler(func=AAS)
def send_price(message):
    print("checking which command was passed")
    com = message.text
    com = (re.sub(r'[0-9]', '', com)).strip() #removes all numbers from the message
    com = com.lower()
    print(com)
    if com == "o":
        print("creating a new oriely account")
        e = funRiely()
        msg = ("Here is your o'Riely account: \n"+e[0] + "\n" + e[1])
        print("this is msg " + msg)  # I'm not that good with debugging dont laugh
        bot.send_message(message.chat.id, msg)
    elif com == "c":
        print("creating a new cybrary account")
        e = funCyb()
        msg = ("Here is your cybrary account: \n"+ e[0] + "\n" + e[1])
        print("this is msg " + msg) #I'm not that good with debugging dont laugh
        bot.send_message(message.chat.id, msg)
    else:
        print("invalid command")




bot.polling(none_stop=True, timeout=123)