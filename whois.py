import os


class Whois():
    def wh(self, ip_add):
        ip = 0
        self.ip_add = ip
        var = 2
        while var == 2:
            
            d ="""
            
           _             _      
          | |           (_)     
__      __| |__    ___   _  ___ 
\ \ /\ / /| '_ \  / _ \ | |/ __|
 \ V  V / | | | || (_) || |\__ \
  \_/\_/  |_| |_| \___/ |_||___/
                                
                                

                                                        
                                                        

            
            """
        print(d)
        
        print("Please select from the options below: ")
        print("1. Normal scan")

        print("2. Use the American Registry for Internet Numbers database")
        print("3. Use the Network Abuse Clearinghouse database")
        print("4. Use the US Department of Defense database")

        print("5. Use the Internet Assigned Numbers Authority database")

        print("6. Use the Route Arbiter Database database")
        print("7. Use the Russia Network Information Center database")
        print("8. Use the R'eseaux IP Europ'eens database")
        print("9. Exit")
            
        option = int(input("Please enter your scan option: "))
        vf = (input("[+]Enter Your Web Address or IP: "))
        if(option == 1):
            os.system("whois "+vf)

        elif(option == 2):
            os.system("whois -a "+vf)
        elif(option == 3):
            os.system("whois -b "+vf)
        elif(option == 4):
            os.system("whois -d "+vf)
                #2 3 7 9
        elif(option == 5):
            os.system("whois -I "+vf)

        elif(option == 6):
            os.system("whois -m "+vf)
        elif(option == 7):
            os.system("whois -R "+vf)
        elif(option == 8):
            os.system("whois -r "+vf)

        else:
                var = 3

