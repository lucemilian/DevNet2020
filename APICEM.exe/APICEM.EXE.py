import sys
from time import sleep
#El texto se ha puesto en ingles con el objetivo de practicar el idioma

#Mensaje de bienvenida
startMsg = " STARTING APICEM.exe " 
print(startMsg.center(50,"#"))



# Funcionalidad numero 1
def funcionalidadN1():

    fN1Msg = " I am: " + funcionalidadN1.__name__+" "
    print(fN1Msg.center(40,"*"))
    
    sleep(5)
    return

# Funcionalidad numero 2    
def funcionalidadN2():

    fN2Msg = " I am: " + funcionalidadN2.__name__+" "
    print(fN2Msg.center(40,"*"))
    
    sleep(5)
    return

# Funcionalidad numero 3
def funcionalidadN3():

    fN3Msg = " I am: " + funcionalidadN3.__name__+" "
    print(fN3Msg.center(40,"*"))
    
    sleep(5)
    return

# Funcionalidad numero 4    
def funcionalidadN4():

    fN4Msg = " I am: " + funcionalidadN4.__name__+" "
    print(fN4Msg.center(40,"*"))
    
    sleep(5)
    return

def bye():
    sys.exit("Exiting...")

switcher = {
        1: funcionalidadN1,
        2: funcionalidadN2,
        3: funcionalidadN3,
        4: funcionalidadN4,
        5: bye
    }

# El buen main...menú
def main():

    mainMsg=" MAIN MENU "

    while True:         
        print(mainMsg.center(40,"*"))
        
        print ("-[1] OPTION 1\n-[2] OPTION 2\n-[3] OPTION 3\n-[4] OPTION 4\n-[5] EXIT")
        vOpera = input("Using numbers, specify the desired operation: ")
        
        print ("\nProcessing...\n")
        
        try:
            func = switcher.get(int(vOpera),)
            func()

        except ValueError as e:
            print ("\nINVALID OPTION!\n")
            pass
        
        pass
    

if __name__ == "__main__":
    main()