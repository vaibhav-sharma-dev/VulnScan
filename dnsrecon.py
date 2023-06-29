import os


class Dnsrecon():
    def dns(self, ip_addr):
        ip = 0
        self.ip_addr = ip
        var = 3
        while var == 3:
            d = """
     _                                    
    | |                                   
  __| |_ __  ___ _ __ ___  ___ ___  _ __  
 / _` | '_ \/ __| '__/ _ \/ __/ _ \| '_ \ 
| (_| | | | \__ \ | |  __/ (_| (_) | | | |
 \__,_|_| |_|___/_|  \___|\___\___/|_| |_|
                                          
            """
            print(d)
            print("1. DNS recon using IP or URL: ")
            print("2. Exit")
            gh = int(input("Enter any of the 2 options: "))
            if(gh == 1):
                print("\033[1;92m")
                print("Type your web address: ")
                vf = (input("Enter Your Web Address or IP: "))
                os.system("dnsrecon -d "+vf)
            else:
                var = 4
