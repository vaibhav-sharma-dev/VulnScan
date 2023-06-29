#!/usr/bin/env python

import whois
import dnsrecon
import scan
import nikto
import hydra
import os
import dirb
import wpscan
import CEwL


#USING ANSI COLORS

RED="\e[31m"
ORANGE="\e[33m"
BLUE="\e[94m"
GREEN="\e[92m"
STOP="\e[0m"

 


s="""

                                                                                                                                               
                                                                                                                                               
VVVVVVVV           VVVVVVVV                 lllllll                     SSSSSSSSSSSSSSS                                                        
V::::::V           V::::::V                 l:::::l                   SS:::::::::::::::S                                                       
V::::::V           V::::::V                 l:::::l                  S:::::SSSSSS::::::S                                                       
V::::::V           V::::::V                 l:::::l                  S:::::S     SSSSSSS                                                       
 V:::::V           V:::::Vuuuuuu    uuuuuu   l::::lnnnn  nnnnnnnn    S:::::S                cccccccccccccccc  aaaaaaaaaaaaa  nnnn  nnnnnnnn    
  V:::::V         V:::::V u::::u    u::::u   l::::ln:::nn::::::::nn  S:::::S              cc:::::::::::::::c  a::::::::::::a n:::nn::::::::nn  
   V:::::V       V:::::V  u::::u    u::::u   l::::ln::::::::::::::nn  S::::SSSS          c:::::::::::::::::c  aaaaaaaaa:::::an::::::::::::::nn 
    V:::::V     V:::::V   u::::u    u::::u   l::::lnn:::::::::::::::n  SS::::::SSSSS    c:::::::cccccc:::::c           a::::ann:::::::::::::::n
     V:::::V   V:::::V    u::::u    u::::u   l::::l  n:::::nnnn:::::n    SSS::::::::SS  c::::::c     ccccccc    aaaaaaa:::::a  n:::::nnnn:::::n
      V:::::V V:::::V     u::::u    u::::u   l::::l  n::::n    n::::n       SSSSSS::::S c:::::c               aa::::::::::::a  n::::n    n::::n
       V:::::V:::::V      u::::u    u::::u   l::::l  n::::n    n::::n            S:::::Sc:::::c              a::::aaaa::::::a  n::::n    n::::n
        V:::::::::V       u:::::uuuu:::::u   l::::l  n::::n    n::::n            S:::::Sc::::::c     ccccccca::::a    a:::::a  n::::n    n::::n
         V:::::::V        u:::::::::::::::uul::::::l n::::n    n::::nSSSSSSS     S:::::Sc:::::::cccccc:::::ca::::a    a:::::a  n::::n    n::::n
          V:::::V          u:::::::::::::::ul::::::l n::::n    n::::nS::::::SSSSSS:::::S c:::::::::::::::::ca:::::aaaa::::::a  n::::n    n::::n
           V:::V            uu::::::::uu:::ul::::::l n::::n    n::::nS:::::::::::::::SS   cc:::::::::::::::c a::::::::::aa:::a n::::n    n::::n
            VVV               uuuuuuuu  uuuullllllll nnnnnn    nnnnnn SSSSSSSSSSSSSSS       cccccccccccccccc  aaaaaaaaaa  aaaa nnnnnn    nnnnnn
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
                                                                                                                                               
"""
 
# print("\033[1;50m",s)
print("\033[1;93m",s)

ip_add=input("[+] Enter the IP Address > ")
response=os.system("ping -c 5 "+ip_add+">ip.txt")

#READ THE FILE ip.txt

f=open("ip.txt","r")
response=(f.read())
#print(response)
print("\033[1;39m")
if "icmp" in response:
    

    r=1
    while r==1:
        print("\033[1;33m",s)
        print("\033[1;39m")
        print("------------------------------------YOUR WEBSITE IS UP WHAT FURTHER YOU WANT TO DO--------------------------------------")
        print("1 Nmap")
        print("2 whois")
        print("3 dnsrecon")
        print("4 dirb")
        print("5 CEwL")
        print("6 nikto")
        print("7 hydra")
        print("8 wpscan")
        print("9 exit")
        input_from_user=int(input("[+] Enter a number from 1 to 9 >"))
        if input_from_user==1:
            
             obj=scan.Nmap()
             obj.nmpa(ip_add)
        elif input_from_user==2:
            obj=whois.Whois()
            obj.wh(ip_add)
        elif input_from_user==3:
            obj=dnsrecon.Dnsrecon()
            obj.dns(ip_add)
        elif input_from_user==4:
            obj=dirb.Dirb()
            obj.dir(ip_add)
        elif input_from_user==5:
            obj=CEwL.Cewl()
            obj.cew(ip_add)
        elif input_from_user==6:
            obj=nikto.Nikto()
            obj.nik(ip_add)
        elif input_from_user==7:
            obj=hydra.Hydra()
            obj.Hyd(ip_add)
        elif input_from_user==8:
            obj=wpscan.Wpscan()
            obj.wpsc(ip_add)
        elif input_from_user>9:
            print("Enter valid number ")
        else:
            r=2
            print("\033[1;33m""[+] Your program has been terminated")
else:
    print("[*] PLEASE CHECK YOUR INTERNET")
