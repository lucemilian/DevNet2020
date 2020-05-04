import sys
import requests
import time
import json
import urllib3
from time import sleep
from netmiko import ConnectHandler



#El texto se ha puesto en ingles con el objetivo de practicar el idioma

#Mensaje de bienvenida
startMsg = " STARTING MyCSR1000v" 
print(startMsg.center(50,"$"))

#Credenciales
username="cisco"
password="cisco123!"
sTicket=""

# Funcionalidad para OBTENER listado de las interfaces del router
def routerINTget():

    fN0Msg = " I am: " + routerINTget.__name__+" "
    print(fN0Msg.center(40,"*"))

    
    
    
    sleep(3)
    return

# Funcionalidad para CREAR interfaces del router
def routerINTmake():

    fN1Msg = " I am: " + routerINTmake.__name__+" "
    print(fN1Msg.center(40,"*"))
    
    
    sleep(3)
    return

# Funcionalidad para BORRAR interfaces del router
def routerINTdestroy():

    fN2Msg = " I am: " + routerINTdestroy.__name__+" "
    print(fN2Msg.center(40,"*"))
    
    
    sleep(3)
    return

# Funcionalidad para manipular tabla de enrutado del router
def routerROUTING():

    fN3Msg = " I am: " + routerROUTING.__name__+" "
    print(fN3Msg.center(40,"*"))
    

    
    sleep(3)
    return


# Funcionalidad para realizar petición a 2 módulos de yang diferentes
def routerTOyang():

    fN4Msg = " I am: " + routerTOyang.__name__+" "
    print(fN4Msg.center(40,"*"))
    
    
    
    sleep(3)
    return




def bye():
    sys.exit("Exiting...")

switcher = {
        0: routerINTget,
        1: routerINTmake,
        2: routerINTdestroy,
        3: routerROUTING,
        4: routerTOyang,
        5: bye
    }

# El buen main...menú
def main():

    mainMsg=" MAIN MENU "

    requests.packages.urllib3.disable_warnings()

    while True:         
        print("\n",mainMsg.center(40,"*"))
        
        print ("-[0] Get list of router's interfaces",
        "\n-[1] Create interface",
        "\n-[2] Delete interface",
        "\n-[3] Configure routing table",
        "\n-[4] Call other modules to YANGOUT",
        "\n-[5] EXIT")
        vOpera = input("Using numbers, specify the desired operation: ")
        
        print ("\nProcessing...\n")
        
        try:
            func = switcher.get(int(vOpera),)
            func()

        except ValueError as e:
            print(e)
            print ("\nINVALID OPTION!\n")
            pass
        
        pass
    

if __name__ == "__main__":
    main()