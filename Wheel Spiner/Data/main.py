#-------------#
#Pre Requirements
import os
#-------------#
#-------------#
#Imports
import time
import random
#-------------#
#logo
print("v1 by mg")
print("██╗    ██╗██╗  ██╗███████╗███████╗██╗       ")  
print("██║    ██║██║  ██║██╔════╝██╔════╝██║       ")  
print("██║ █╗ ██║███████║█████╗  █████╗  ██║       ")  
print("██║███╗██║██╔══██║██╔══╝  ██╔══╝  ██║       ")  
print("╚███╔███╔╝██║  ██║███████╗███████╗███████╗  ")  
print(" ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝  ") 
                                             
print("███████╗██████╗ ██╗███╗   ██╗███████╗██████╗ ") 
print("██╔════╝██╔══██╗██║████╗  ██║██╔════╝██╔══██╗") 
print("███████╗██████╔╝██║██╔██╗ ██║█████╗  ██████╔╝") 
print("╚════██║██╔═══╝ ██║██║╚██╗██║██╔══╝  ██╔══██╗") 
print("███████║██║     ██║██║ ╚████║███████╗██║  ██║") 
print("╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝") 
print("")
#-------------# 
#Functions                        
def createNewWheel():
    os.system("cls")
    print("Whats the Wheel Name?")
    wheelname = input(">>>")        
    print("Whats the 1 object?")
    wheel1obj = input(">>>") 
    print("Whats the 2 object?")
    wheel2obj = input(">>>")    
    print("Whats the 3 object?")
    wheel3obj = input(">>>")  

    wheelobjects = [
        wheel1obj,
        wheel2obj,
        wheel3obj
    ]       
    time.sleep(1)
    print(wheelname) 
    print(" ") 
    input("Press Enter to spin the wheel")     
    print(random.choice(wheelobjects)) 
    input("Press Enter to quit")     
            
 

#-------------#
#MENU 1



def menu1():
    m1opt = 0
    print("What do you want to do?")
    print("[1]New Wheel")
    print("[2]Saved Wheels")
    print("[3]Quit")
    m1opt = (input(">>>"))
    if m1opt == "1":
        createNewWheel()
    else:
        if m1opt == "2":  
           os.system("cls")
           print("Coming soon!")
           time.sleep(3)
           os.system("cls")
           menu1()   
        else:
             if m1opt == "3":
                 quit
             else:
                 print("This was not any of the options!")
                 time.sleep(3)
                 os.system("cls")
                 menu1()
menu1()   



#-------------# 
#Functions                        
def createNewWheel():
    os.system("cls")
    print("Whats the Wheel Name?")
    wheelname = input(">>>")        
    print("Whats the 1 object?")
    wheel1obj = input(">>>") 
    print("Whats the 2 object?")
    wheel2obj = input(">>>")    
    print("Whats the 3 object?")
    wheel3obj = input(">>>")  

    wheelobjects = [
        wheel1obj,
        wheel2obj,
        wheel3obj
    ]                   
    def spiner():
        print(wheelname) 
        print(" ") 
        input("Press Enter to spin the wheel")     
        print(random.choice(wheelobjects)) 
        input("Press Enter to quit")         

                                             
                                             
                                             
                                             

