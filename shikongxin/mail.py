#!/usr/bin/python3

import smtplib

sender = '40089056@qq.com'
receivers = ['40089056@qq.com']


message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
From your king
"""


smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
smtpObj.login("40089056@qq.com", "mijwhzivsxjkbhef")

smtpObj.sendmail(sender, receivers, message)
# print("Successfully sent email")
