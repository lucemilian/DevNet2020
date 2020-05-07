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

def clockReset():
    sshovercli = ConnectHandler(device_type="cisco_ios",host="192.168.56.101",port=22,username=username,password=password)

    #Clock reset
    outputClock = sshovercli.send_command("clock set 00:00:01 1 January 2000")
    print("Clock reset:\n{}".format(outputClock))

    #Envio de conjunto de intrucciones
    configCommands= ("no netconf-yang","netconf-yang","no restconf","restconf")
    outputConfig = sshovercli.send_config_set(configCommands)
    print("Config output from device:\n{}".format(outputConfig))    
    
    #Desconectamos
    sshovercli.disconnect()

    return


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
    
    #Connection address
    urlInterfaces = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface"
    urlIntState = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces-state/interface"

    #Headers
    headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}
    
    #Authentication
    basic_auth=(username,password)

    rInterfaces = requests.get(urlInterfaces, auth=basic_auth,headers=headers, verify=False)
    rIntState = requests.get(urlIntState, auth=basic_auth,headers=headers, verify=False)
    print("Requests statuses: ", rInterfaces.status_code," || ",rIntState.status_code,"\n")

    rJSON=rInterfaces.json()
    rJSON_IS=rIntState.json()
    # print(rJSON_IS)

    
    dash="-"

    print("-".center(110,"-"))
    print('{:<20s}{:>20s}{:>20s}{:>20s}{:^10s}{:^10s}{:^10s}'.format("Name","MAC address","IP Address","NetMask","Admin","Oper","Enabled"))
    print("-".center(110,"-"))

   
    """     counter=0
        #Recogemos otros datos sobre las interfaces
        for m in rJSON_IS['ietf-interfaces:interface']
        
            #Sacamos los valores de restconf/data/ietf-interfaces:interfaces-state
            nameIS=rJSON_IS['ietf-interfaces:interface'][counter]['name']
            adminStat=rJSON_IS['ietf-interfaces:interface'][counter]['admin-status']
            operStat=rJSON_IS['ietf-interfaces:interface'][counter]['oper-status']
            macAddress=rJSON_IS['ietf-interfaces:interface'][counter]['phys-address']
            counter+=1
    """
    
    counter=0
    nameInt,enabled,ipAddress,subnetMask=[],[],[],[]
    adminStat,macAddress,operStat=[],[],[]
    
    #Recogemos las interfaces y debido a como ietf-interfaces estrcutura los datos, sus subinterfaces
    for i in rJSON['ietf-interfaces:interface']:  
        
        nameInt.append(rJSON['ietf-interfaces:interface'][counter]['name'])
        
        #Buscamos si tiene una dirreccion física, ya que puede ser una subinterfaz
        #Aunque creo que no haria falta ya que parece haber un indice que los iguala en nivel "if-index"
        subCount=0
        sifound=False
        for l in rJSON_IS['ietf-interfaces:interface']:
            if nameInt[counter]==rJSON_IS['ietf-interfaces:interface'][subCount]['name']:
                #Si tiene dir fisica se guarda al mismo nivel
                adminStat.append(rJSON_IS['ietf-interfaces:interface'][subCount]['admin-status'])
                operStat.append(rJSON_IS['ietf-interfaces:interface'][subCount]['oper-status'])
                macAddress.append(rJSON_IS['ietf-interfaces:interface'][subCount]['phys-address'])
                subCount+=1
                sifound=True
                break
        
        #Se rellena lo que falte
        if sifound==False:
            adminStat.append(dash)
            operStat.append(dash)
            macAddress.append(dash)
        
        #Intentamos pillar los "KeyWord-Error", por ejemplo, una nueva interfaz no se le a declarado la ip.
        try:
            #Sacamos los valores de restconf/data/ietf-interfaces:interfaces
            enabled.append(rJSON['ietf-interfaces:interface'][counter]['enabled'])
            ipAddress.append(rJSON['ietf-interfaces:interface'][counter]['ietf-ip:ipv4']['address'][0]['ip'])
            subnetMask.append(rJSON['ietf-interfaces:interface'][counter]['ietf-ip:ipv4']['address'][0]['netmask'])

        except KeyError as e:
            #Ponemos como "NULL" en caso de que salte
            ipAddress.append("NULL")
            subnetMask.append("NULL")
            pass
        
        #Imprimimos la tabla        
        print('{:<20s}{:>20s}{:>20s}{:>20s}{:^10s}{:^10s}{:^10b}'.format(nameInt[counter],macAddress[counter],ipAddress[counter],subnetMask[counter],adminStat[counter],operStat[counter],enabled[counter]))
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
    configCommands= (firstC,secondC,description,"no shutdown")
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
        intCounter+=1
    
    vIP = input("Specify desired IP address, default ""192.168.0.X"": ")
    if vIP=="":
        global globalIP
        vIP=str(globalIP)
        print (vIP)
        globalIP+=255
    
    vMask = input("Specify desired Mask, default is ""/24"": ")
    if vMask=="":
        vMask="255.255.255.0"

    vDesc = input("Specify desired Description, default is ""IntType+IP"": ")
    if vDesc=="":
        vDesc="description "+vTYPE+" "+vIP


    #Conectamos al dispositivo
    print("Connecting...")
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
    
    #Miramos las interfaces existentes
    routerINTget()

    #Definimos variables del set de instrucciones
    vToDelete = input("Specify desired interface by NAME: ")
    if vToDelete=="":
        global intCounter
        vToDelete="Loopback"+str(intCounter-1)

    #Connection address
    url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface="+vToDelete

    #Headers
    headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}
    
    #Authentication
    basic_auth=(username,password)

    resp = requests.delete(url, auth=basic_auth,headers=headers, verify=False)
    print("Request status: ", resp.status_code)
    
    sleep(3)
    return

    #
        #
            #
                #
            #
        #
    #


# Funcionalidad para mostrar la tabla de enrutado del router
def routerROUTING():

    fN3Msg = " I am: " + routerROUTING.__name__+" "
    print(fN3Msg.center(40,"*"))
        
    #Connection address
    # url = "https://192.168.56.101/restconf/data/ietf-routing:routing-state"
    # url="https://192.168.56.101/restconf/data/ietf-routing:routing-state/routing-instance=default/ribs/rib"
    url = "https://192.168.56.101/restconf/data/ietf-routing:routing-state/routing-instance=default/ribs/rib=ipv4-default/routes/route"

    #Headers
    headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}
    
    #Authentication
    basic_auth=(username,password)

    resp = requests.get(url, auth=basic_auth,headers=headers, verify=False)
    print("Request status: ", resp.status_code)


    rJSON=resp.json()

    counter=0
    dash="-"
    # print (rJSON)
   
    for i in rJSON['ietf-routing:route']:
        if counter == 0:
            print("\n","-".center(60,"-"))
            print('{:^5s}{:^10s}{:>20s}{:>20s}'.format("#","RPref","Destination Prefix","Outgoing Interface"))
            print("-".center(60,"-"))
            
        print('{:^5d}{:^10d}{:>20s}{:>20s}'.format(counter,
                                        rJSON['ietf-routing:route'][counter]['route-preference'],
                                        rJSON['ietf-routing:route'][counter]['destination-prefix'],
                                        rJSON['ietf-routing:route'][counter]['next-hop']['outgoing-interface']))
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


def routerSubINTget():

    fN4Msg = " I am: " + routerSubINTget.__name__+" "
    print(fN4Msg.center(40,"*"))
    
    #Connection address
    urlInterfaces = "https://192.168.56.101/restconf/data/openconfig-interfaces:interfaces/interface"
    urlBasSubInt = "https://192.168.56.101/restconf/data/openconfig-interfaces:interfaces/interface="
    urlAddSubInt ="/subinterfaces/subinterface"
    uraAddAddSI ="/state"
    
    #Headers
    headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}
    
    #Authentication
    basic_auth=(username,password)

    rInterfaces = requests.get(urlInterfaces, auth=basic_auth,headers=headers, verify=False)
    print("Requests statuses: ", rInterfaces.status_code,"\n")

    rJSON=rInterfaces.json()
    
    counter=0
    dash="-"

    #Listamos las interfaces
    for i in rJSON['openconfig-interfaces:interface']:
        if counter == 0:
            print("-".center(80,"-"))
            print('{:<20s}{:>20s}{:>40s}'.format("Interface","Subinterface", "Description"))
            print("-".center(80,"-"))

        nameInt=rJSON['openconfig-interfaces:interface'][counter]['name']
        
        tempUrl=urlBasSubInt+nameInt+urlAddSubInt
        # print(tempUrl)
        rSubInt = requests.get(tempUrl, auth=basic_auth,headers=headers, verify=False)
        rJSON_SI=rSubInt.json()
        # print(rJSON_SI)
        
        countSubs=0
        #Listamos las subinterfaces
        for x in rJSON_SI['openconfig-interfaces:subinterface'] :
            
            name_SI=rJSON_SI['openconfig-interfaces:subinterface'][countSubs]['state']['name']
            try:
                desc_SI=rJSON_SI['openconfig-interfaces:subinterface'][countSubs]['state']['description']
            except KeyError as e:
                name_SI=rJSON_SI="Null"
                pass
            
                    #Imprimimos la tabla        
            print('{:<20s}{:>20s}{:>40s}'.format(nameInt,name_SI,desc_SI))
            countSubs+=1
        
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


def routerUsersget():

    fN5Msg = " I am: " + routerUsersget.__name__+" "
    print(fN5Msg.center(40,"*"))
    
    requests.packages.urllib3.disable_warnings()

    #Connection address
    urlUsername = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/username"
        
    #Headers
    headers = {'Accept': 'application/yang-data+json','Content-Type': 'application/yang-data+json'}
    
    #Authentication
    basic_auth=(username,password)

    rUsernames = requests.get(urlUsername, auth=basic_auth,headers=headers, verify=False)
    print("Requests statuses: ", rUsernames.status_code,"\n")

    rJSON_U=rUsernames.json()
    
    counter=0
    dash="-"
    for i in rJSON_U['Cisco-IOS-XE-native:username']:
        if counter == 0:
            print("-".center(60,"-"))
            print('{:<20s}{:^10s}{:^10s}{:>20s}'.format("Name","Privilge", "Encryp","Password"))
            print("-".center(60,"-"))

        nameU=rJSON_U['Cisco-IOS-XE-native:username'][counter]['name']
        privilege=rJSON_U['Cisco-IOS-XE-native:username'][counter]['privilege']
        encryption=rJSON_U['Cisco-IOS-XE-native:username'][counter]['password']['encryption']
        passU=rJSON_U['Cisco-IOS-XE-native:username'][counter]['password']['password']

        print('{:<20s}{:^10d}{:^10s}{:>20s}'.format(nameU,privilege,encryption,passU))
        
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


# Funcionalidad para realizar petición a 2 módulos de yang diferentes
def routerTOyang():

    fN4Msg = " I am: " + routerTOyang.__name__+" "
    print(fN4Msg.center(40,"*"))
    
    
    





def bye():
    sys.exit("Exiting...")

switcher = {
        0: clockReset,
        1: routerINTget,
        2: routerINTmake,
        3: routerINTdestroy,
        4: routerROUTING,
        5: routerSubINTget,
        6: routerUsersget,
        7: bye
    }

# El buen main...menú
def main():

    requests.packages.urllib3.disable_warnings()
    mainMsg=" MAIN MENU "

    while True:         
        print("\n",mainMsg.center(40,"*"))
        
    
        print ("\n-[0] RESET THE CLOCK",
        "\n-[1] Get list of router's interfaces",
        "\n-[2] Create interface",
        "\n-[3] Delete interface",
        "\n-[4] Configure routing table",
        "\n-[5] Get list of router's subinterfaces",
        "\n-[6] Get list of router's users",
        "\n-[7] EXIT")
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