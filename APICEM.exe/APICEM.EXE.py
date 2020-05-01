import sys
import requests
import time
import json
import urllib3
from time import sleep

#El texto se ha puesto en ingles con el objetivo de practicar el idioma

#Mensaje de bienvenida
startMsg = " STARTING APICEM.exe " 
print(startMsg.center(50,"#"))

#urls 
urlTicket = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
urlGen = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/"

#Credenciales
username="devnetuser"
password="Xj3BDqbU"
sTicket=""

# Funcionalidad que dice el próximo paso del ISS, por defecto, sobre Getafe
def ISSpass():

    fN0Msg = " I am: " + ISSpass.__name__+" "
    print(fN0Msg.center(40,"*"))
    
    vLatitude = input("Give desired LATITUDE, or press [ENTER]: ")
    if vLatitude == "":
        latitude = "40.305012"
    else:
        try:
            latitude = float(vLatitude)

        except ValueError:
            print ("Wrong format...using default.")
            latitude = "40.305012"
    
    vLongitude = input("Give desired LONGITUDE, or press [ENTER]: ")
    if vLongitude == "":
        longitude = "-3.732700"
    else:
        try:
            longitude= float(vLongitude)

        except ValueError:
            print ("Wrong format...using default.")
            longitude = "-3.732700"


    #urlExample= "http://api.open-notify.org/iss/v1/?lat=30.26715&lon=-97.74306"

    urlMod = "http://api.open-notify.org/iss/v1/?lat="+latitude+"&lon="+longitude
    # print(urlMod) #Al parecer usar comas en vez de plus convierte urlMod en una lista
    
    json_data = requests.get(urlMod).json()
    
    print(json_data)
    epoch = json_data['response'][1]['risetime']
    print (epoch)
    next_pass = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
    print("\nThe next ISS pass, over: \n    LAT: ",latitude,"\n    LONG: ",longitude,"\nWill be at: ",(next_pass))

    print("\n")
    sleep(5)
    return

# Funcionalidad para pedir ticket de servicio al APICEM
def GET_TICKET():

    fN1Msg = " I am: " + GET_TICKET.__name__+" "
    print(fN1Msg.center(40,"*"))

    # requests.packages.urllib3.disable_warnings()
    
    headers={
        'Content-Type':'application/json'
    }

    body_json={
        "password": password,
        "username": username
    }
    
    resp = requests.post(urlTicket,json.dumps(body_json),headers=headers,verify=False)
    response_json = resp.json()
    
    global sTicket
    sTicket = response_json["response"]["serviceTicket"]

    print("Ticket request status", resp.status_code)
    print("The Service Ticket is: ", sTicket)

 
    # print("\n")
    # sleep(5)
    return

# Funcionalidad que devuelve los hosts de la red
def GET_HOSTS():

    fN2Msg = " I am: " + GET_HOSTS.__name__+" "
    print(fN2Msg.center(40,"*"))

    urlTemp=urlGen+"host"

    print("With service ticket: ",sTicket)

    headers={
        'Content-Type':'application/json',
        'X-Auth-Token': sTicket
    }
    resp = requests.get(urlTemp,headers=headers,verify=False)
    print("Query request status:", resp.status_code)

    rJSON = resp.json()
    #print(rJSON)

    counter=0
    for i in rJSON['response']:
        print("The device with IP:", rJSON['response'][counter]['hostIp'], "hast the MAC:",rJSON['response'][counter]['hostMac'],"and belong to VLAN:",rJSON['response'][counter]['vlanId'])
        counter+=1


    # print("\n")  
    sleep(2)
    return

# Funcionalidad que devuelve los dispositivos de la red
def GET_NET_DEVICES():

    fN3Msg = " I am: " + GET_NET_DEVICES.__name__+" "
    print(fN3Msg.center(40,"*"))

    urlTemp=urlGen+"network-device"

    print("With service ticket: ",sTicket)

    headers={
        'Content-Type':'application/json',
        'X-Auth-Token': sTicket
    }
    resp = requests.get(urlTemp,headers=headers,verify=False)
    print("Query request status:", resp.status_code)

    rJSON = resp.json()
    #print(rJSON)

    counter=0
    for i in rJSON['response']:
        print("The", rJSON['response'][counter]['hostname'],
        "with MAC",rJSON['response'][counter]['macAddress'],
        "belongs to the", rJSON['response'][counter]['family'],
        "family, from the", rJSON['response'][counter]['type'],"series")
        counter+=1
    
    totalND="TOTAL NET-DEVICES: "+str(counter)
    print(totalND.center(40,"="))

    # print("")
    sleep(3)
    return

# Funcionalidad que devuelve el último analisis de flujo ejecutado   
def GET_FLOW_ANALYSIS():

    fN4Msg = " I am: " + GET_FLOW_ANALYSIS.__name__+" "
    print(fN4Msg.center(40,"*"))

    urlTemp=urlGen+"flow-analysis"

    print("With service ticket: ",sTicket)

    headers={
        'Content-Type':'application/json',
        'X-Auth-Token': sTicket
    }
    resp = requests.get(urlTemp,headers=headers,verify=False)
    print("Query request status:", resp.status_code)

    rJSON = resp.json()

    counter=0
    completed=0
    for i in rJSON['response']:

        # Transformamos el lastUpdateTime pdate a una fecha
        lUT = rJSON['response'][counter]['lastUpdateTime']
        lUT/=1000 #el valor no está en milisegundos....
        # print(lUT)
        lastFlowCheck = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(lUT))


        if rJSON['response'][counter]['status']=="COMPLETED":
            print ("\nThe device with IP:", rJSON['response'][counter]['sourceIP'],
            "\ncan reach device with IP",rJSON['response'][counter]['destIP'],
            "\nas of last check on:", lastFlowCheck)
            completed+=1

        if rJSON['response'][counter]['status']=="FAILED":
            print ("\nThe device with IP:", rJSON['response'][counter]['sourceIP'],
            "\nCAN'T reach device with IP",rJSON['response'][counter]['destIP'],
            "\nas of last flow check on:", lastFlowCheck)

        if rJSON['response'][counter]['status']=="IN PROGRESS":
            print ("\nFlow check of the device with IP:", rJSON['response'][counter]['sourceIP'],
            "\n TO the device with IP",rJSON['response'][counter]['destIP'],
            "\nis still:",rJSON['response'][counter]['status'])

        counter+=1
    
    totalND="TOTAL OPEN FLOWS: "+str(completed)+"/"+str(counter)
    print(totalND.center(40,"="))

    # print("\n")
    sleep(3)
    return

def bye():
    sys.exit("Exiting...")

switcher = {
        0: ISSpass,
        1: GET_TICKET,
        2: GET_HOSTS,
        3: GET_NET_DEVICES,
        4: GET_FLOW_ANALYSIS,
        5: bye
    }

# El buen main...menú
def main():

    mainMsg=" MAIN MENU "

    requests.packages.urllib3.disable_warnings()

    while True:         
        print("\n",mainMsg.center(40,"*"))
        
        print ("-[1] GET TICKET\n-[2] GET HOSTS\n-[3] GET NETWORK DEVICES\n-[4] GET FLOW ANALYSIS\n-[5] EXIT")
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