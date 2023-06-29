#!/usr/bin/eny python

import os


class Hydra():
    def Hyd(self, ip):
        print("\033[1;32m")
        self.ip_add = ip

        var = 1
        while var == 1:
            d = """
 _               _           
| |             | |          
| |__  _   _  __| |_ __ __ _ 
| '_ \| | | |/ _` | '__/ _` |
| | | | |_| | (_| | | | (_| |
|_| |_|\__, |\__,_|_|  \__,_|
        __/ |                
       |___/                 
"""
            print(d)
            print("[+] 1 Generate your own password list ")
            print("[+] 2 use prebuild password list ")
            print("[+] 3 exit ")
            input_for_list = int(input("[+] Enter your choice "))
            if input_for_list == 1:
                username_list = input("[+] Enter the name of your Username file (with .txt extension)  > ")
                print("--------------UserNameList-------------")
                os.system("cat>"+username_list)
                print("")
                print("--------------PassWordList-------------")
                password_list = input("[+] Enter the name of your Password file (with .txt extension) > ")
                print("")
                os.system("cat>"+password_list)
                print("")
                print("[+]You created userName and passWord list successfully  ")
                print("")

                print(
                    "[+] This is your currentWorking Directory and your Dictionary you created > ")
                print(os.system("pwd;find *.txt"))
                print("")
                protocol = input(
                    "[+] Enter the service running from your end ssh or ftp > ")

                ip_version = input(
                    "[+] Enter version of ip (4 for ipv4 or 6 for ipv6) > ")
                os.system("hydra -L "+username_list+" -P "+password_list +
                          " "+ip + " "+protocol+" -t "+ip_version+" -V -F")

            elif input_for_list == 2:

                username_list = input("[+] Enter UserName Directory > ")
                password_list = input("[+] Enter PassWord Directory > ")
                protocol = input(
                    "[+] Enter the service running from your end ssh or ftp > ")
                ip_version = input(
                    "[+] Enter version of ip (4 for ipv4 or 6 for ipv6) > ")
                os.system("hydra -L "+username_list+" -P "+password_list +
                          " "+ip + " "+protocol+" -t "+ip_version+" -V -F")

            elif input_for_list == 3:
                var = 2
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
