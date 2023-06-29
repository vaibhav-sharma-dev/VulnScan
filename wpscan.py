#!/usr/bin/eny python
import os
#test commit

class Wpscan():
    def wpsc(self, ip):
        self.ip_add = ip
        print("\033[1;94m")

        var = 1
        while var == 1:
            d = """
            __      ___ __  ___  _
\ \ /\ / / '_ \/ __|/ __/ _` | '_ \ 
 \ V  V /| |_) \__ \ (_| (_| | | | |
  \_/\_/ | .__/|___/\___\__,_|_| |_|
         | |                        
         |_|                        
         """
            print(d)
            print(f"[+] 1 for {ip}")
            print("[+] 2 URL of your WordPress")
            print("[+] 3 Exit")
            input_for_wpscan = int(input("Enter number from 1 to 3 > "))
            if input_for_wpscan == 1:
                var1 = 1
                while var1 == 1:

                    print("[+] 1 Generate your own passWord list ")
                    print("[+] 2 use inbuild password list ")
                    print("[+] 3 Exit ")
                    input_for_list = int(input("[+] Enter your choice "))
                    if input_for_list == 1:

                        username_list = input(
                            "[+] Enter the name of your Username file (with .txt extension)  > ")
                        print("--------------UserNameList-------------")
                        os.system("cat>"+username_list)
                        print("")

                        password_list = input(
                            "[+] Enter the name of your Password file (with .txt extension) > ")
                        print("--------------PassWordList-------------")
                        os.system("cat>"+password_list)
                        print("")
                        print(
                            "[+]You created userName and passWord list successfully  ")
                        print("")

                        print(
                            "[+] This is your currentWorking Directory and your Dictionary you created > ")
                        print(os.system("pwd;find *.txt"))
                        print("")
                        os.system("sudo wpscan -U "+username_list +
                                  "-P "+password_list+" --url http://"+ip)

                    elif input_for_list == 2:

                        username_list = input(
                            "[+] Enter UserName Directory > ")
                        password_list = input(
                            "[+] Enter PassWord Directory > ")
                        os.system("sudo wpscan -U "+username_list +
                                  "-P "+password_list+" --url http://"+ip)

                    elif input_for_list == 3:
                        var1 = 2
                        print(" ")
                        print(" ")

                    else:
                        print("")
                        print("")
                        print("")
                        print(
                            "\033[1;41m[*] Please Enter valid number \033[1;40m")
                        print("")
                        print("")
                        print("")
            elif input_for_wpscan == 2:

                input_wp_url = input("[+] Enter URL of your WordPress > ")
                input_for_wpscan1 = input("[+] Ente http or https > ")
                username_list = input("[+] Enter UserName Directory > ")
                password_list = input("[+] Enter PassWord Directory > ")

                if input_for_wpscan1 == "http":
                    os.system("sudo wpscan -U "+username_list+"-P " +
                              password_list+" --url http://"+input_wp_url)
                else:
                    os.system("sudo wpscan -U "+username_list+"-P " +
                              password_list+" --url https://"+input_wp_url)

            elif input_for_wpscan == 3:
                var = 2
                print(" ")
                print(" ")
                print("\033[1;34m-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\033[1;34m---------------------------------------------------------------------------------------------!WpScan completed successfully!--------------------------------------------------------------------------------------------------------------")
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
