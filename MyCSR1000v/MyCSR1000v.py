import sys,time
import requests , json, urllib3
from time import sleep
from netmiko import ConnectHandler
import ipaddress


#El texto se ha puesto en ingles con el objetivo de practicar el idioma

#Mensaje de bienvenida
startMsg = " STARTING MyCSR1000v" 
print(startMsg.center(50,"$"))

#Credenciales
username="lucemilian"
password="devnet2020!"
routerIP="192.168.56.101"

#Globals
intCounter=0
globalIP=ipaddress.ip_address("192.168.0.1")


    #
        #
            #
                #
            #
        #
    #




# Funcionalidad para OBTENER listado de las interfaces del router
def routerINTget():

    fN0Msg = " I am: " + routerINTget.__name__+" "
    print(fN0Msg.center(40,"*"))

    requests.packages.urllib3.disable_warnings()

    #Connection address
    url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface"

    #Headers
    headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}
    
    #Authentication
    basic_auth=(username,password)

    resp = requests.get(url, auth=basic_auth,headers=headers, verify=False)
    print("Request status", resp.status_code)


    rJSON=resp.json()

    """ Obtener un listado de las interfaces del router
    (indicar, en modo tabla, el nombre de la interfaz, su IP y MAC) """

    counter=0
    dash="-"
    # print (rJSON)
    
    for i in rJSON['ietf-interfaces:interface']:
        if counter == 0:
            print("\n","-".center(60,"-"))
            print('{:<20s}{:>20s}{:>20s}'.format("Name","IP Address","NetMask"))
            print("-".center(60,"-"))
            
        print('{:<20s}{:>20s}{:>20s}'.format(rJSON['ietf-interfaces:interface'][counter]['name'],
                                        rJSON['ietf-interfaces:interface'][counter]['ietf-ip:ipv4']['address'][0]['ip'],
                                        rJSON['ietf-interfaces:interface'][counter]['ietf-ip:ipv4']['address'][0]['netmask']))
        counter+=1
    
    
    
    sleep(3)
    return

    #
        #
            #
                #
            #
        #
    #


def showIPintB(sshovercli):
    output3 = sshovercli.send_command("show ip interface brief")
    print("show ip interface brief:\n{}".format(output3))


def createLOSSH(sshovercli, intType, ipAdd, theMask, description):

    #
    firstC = "int "+intType
    secondC = "ip address "+ipAdd+" "+theMask
    
    #Set de instrucciones de configuracion
    configCommands= (firstC,secondC,description)
    outputConfig = sshovercli.send_config_set(configCommands)
    print("Config output from device:\n{}".format(outputConfig))

    #Comprobamos que se ha realizado bien
    showIPintB(sshovercli)





# Funcionalidad para CREAR interfaces del router
def routerINTmake():

    fN1Msg = " I am: " + routerINTmake.__name__+" "
    print(fN1Msg.center(40,"*"))
    
    
    #Definimos variables del set de instrucciones
    vTYPE = input("Specify desired interface TYPE, default is ""Loopback X"": ")
    if vTYPE=="":
        global intCounter
        vTYPE="Loopback "+str(intCounter)
    
    vIP = input("Specify desired IP address, default ""192.168.0.X"": ")
    if vIP=="":
        global globalIP
        vIP=str(globalIP)
        print (vIP)
        globalIP+=1
    
    vMask = input("Specify desired Mask, default is ""/24"": ")
    if vMask=="":
        vMask="255.255.255.0"

    vDesc = input("Specify desired Description, default is ""IntType+IP"": ")
    if vDesc=="":
        vDesc="description "+vTYPE+" "+vIP


    #Conectamos al dispositivo
    sshovercli = ConnectHandler(device_type="cisco_ios",host="192.168.56.101",port=22,username=username,password=password)

    #Llamamos a la funcion creadora
    createLOSSH(sshovercli, vTYPE, vIP, vMask, vDesc)
    
    #Desconectamos
    sshovercli.disconnect()

    sleep(3)
    return

    #
        #
            #
                #
            #
        #
    #



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