#!/usr/bin/eny python

import os

class Dirb():
    def dir(self,ip):
        print("\033[1;96m")
        self.ip_add=ip
        d="""
        
     _                     _      
    (   )  .-.              (   )     
  .-.| |  ( _)  __ .-.     | |.-.   
 /   \ |  (''") (   )   \    | /   \  
|  .-. |   | |   | ' .-. ;   |  .-. | 
| |  | |   | |   |  / (_)  | |  | | 
| |  | |   | |   | |         | |  | | 
| |  | |   | |   | |         | |  | | 
| '  | |   | |   | |         | '  | | 
' `-'  /   | |   | |         ' `-' ;  
   `._,'   (_)   (_)          `._.   
                                      
                                      

        """
        ex="""
               use "exit" for exit
            """
        print(d)
        print("")
        print("\033[1;33m",ex,"\033[0;90m")
        print("")
        r=1
        while r==1: 

            input_protocol=input("[+] Enter  http or https >")
            print("")
            
        
            if input_protocol=="http":
                
                os.system("dirb http://"+ip)
                print("")

            elif input_protocol=="https":
                os.system("dirb https://"+ip)
                print("")

            elif input_protocol=="exit":
                print("")
                
                 
                i=input("\033[1;92m[+] Do you want to exit from this program  y/n > \033[0;90m " )
                print("")
                if (i=="y"):
                    r=2
                     
                    
                elif (i=="n"):
                    continue
                else:
                    print("")
                    print("\033[1;41m\033[1;92m[*] Please enter y/n > \033[0;40m \033[0;90m ")
                    print("")
                
            else:
                print("\033[1;39")
                
                print(f"\033[1;41m\033[1;92m[*] You Entered\033[1;39m \"{input_protocol}\"\033[1;92m Please Enter http or https \033[1;40m\033[0;90m")
                print("")
