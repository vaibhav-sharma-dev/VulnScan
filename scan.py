#!/usr/bin/env python


import os

class Nmap():
    def nmpa(self, ip_add):
        ip=input("Please Enter your IP again")
        self.ip_add=ip
        var=1

        sc="""

   _____                       _             
  / ____|                     (_)            
 | (___   ___ __ _ _ __  _ __  _ _ __   __ _ 
  \___ \ / __/ _` | '_ \| '_ \| | '_ \ / _` |
  ____) | (_| (_| | | | | | | | | | | | (_| |
 |_____/ \___\__,_|_| |_|_| |_|_|_| |_|\__, |
                                        __/ |
                                       |___/ 
"""
        


        example="""
        EXAMPLES:
                -v -A 
                -v -sn 
                -v -iR 10000 -Pn -p 80
             """
        
        
        while var==1:
            print("\033[1;35m",sc)
            print("\033[1;33m",example)
            print("\033[1;92m")
            print("-------------------------------Which Type of Scan do you want--------------------------------------")
            print("1 Host Discovery ")
            print("2 Scan(tcp,udp,xmas) ")
            print("3 Service/Version And OS Detection")
            print("4 Script Scan")
            print("5 Aggressive Scanning ")
            print("6 Exit ")
             
            input_from_user1=int(input("[+] Enter your scan type > "))
            if(input_from_user1==1):
                var1=input("[+] use -sL,-sn,-Pn,-PS,-PE for Host Discovery > ")
                os.system("sudo nmap "+var1+" "+ip)
            elif input_from_user1==2:
                var1=input("[+] use -sS,sU,-sN, sI -sY > ")
                os.system("sudo nmap "+var1+" "+ip)

            elif input_from_user1==3:
                var1=input("[+] use -p,-sV,-O,-F,-r > ")
                os.system("sudo nmap "+var1+" "+ip)
            
            elif input_from_user1==4:
                var1=input("[+] use -sC > ")
                os.system("sudo nmap "+var1+" "+ip)
            
            elif input_from_user1==5:
                var1=input("[+] use -A for Aggressive Scanning > ")
                os.system("sudo nmap "+var1+" "+ip)

            elif input_from_user1==6:
                var=2
                print(" ")
                print(" ")
                print("\033[1;34m-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\033[1;34m---------------------------------------------------------------------------------------------!Scanning completed successfully!--------------------------------------------------------------------------------------------------------------")
                print("\033[1;34m-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(" ")
                print(" ")
            else:
                print("")
                print("")
                print("") 
                print("\033[1;41m[*] Please Enter valid number \033[1;40m")
                print("")
                print("")
                print("")
             
         


        
