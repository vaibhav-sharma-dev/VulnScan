import os



class Cewl():
    def cew(self, ip):
        
        self.ip_add = ip
        var=5
        while var==5:
            d="""
  _____ ________          ___      
 / ____|  ____\ \        / / |     
| |    | |__   \ \  /\  / /| |     
| |    |  __|   \ \/  \/ / | |     
| |____| |____   \  /\  /  | |____ 
 \_____|______|   \/  \/   |______|
 """
            print(d)
            print("[+] 1 Enter your IP address/URL ")
            print("[+] 2 Exit")
            vf=int(input("Please enter a number 1 or 2: "))
            if(vf==1):
                print("Please select from the below options: ")
                print("1. Normal scan: ")
                print("2. show the count of each word found: --count or -c")
                print("3. depth search --depth")
                print("4. Include email addresses in search: --email")
                print("5. To keep the downloaded files: --keep")
                print("6. Exit")
                gh=int(input(f"Enter your number:{ip} "))
                if(gh==1):
                    os.system("sudo cewl "+ip)
                elif(gh==2):
                    os.system("sudo cewl "+ip+" --count")
                elif(gh==3):
                    os.system("sudo cewl "+ip+" --depth")
                elif(gh==4):
                    os.system("sudo cewl "+ip+" --email")
                elif(gh==5):
                    os.system("sudo cewl "+ip+" --keep")
                else:
                    var=6                
            else:
                var=6
