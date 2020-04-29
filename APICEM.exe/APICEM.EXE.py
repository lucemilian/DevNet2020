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


#URLs de APIs Disponibles
urlFile = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/file-service"
urlFlowAnalysis = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/policy-analysis"
urlGrouping = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/group"
urlIPGeolocation = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/ipgeo"
urlIPPoolManager = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/ippool"
urlIdentityManager = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/identity-manager "
urlInventory = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/inventory-manager"
urlNetworkDiscovery = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/network-discovery"
urlNetworkPlugPlay = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/ztd"
urlPLIBrokerService = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/pki-broker-service"
urlPolicyAdministration = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/policy-manager"
urlRoleBasedAccessControl = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/rbac-service"
urlScheduler = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/scheduler-service"
urlTask = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/task-service"
urlTopology =   "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/topology"
urlVisibility = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/api-docs/visibility-service"

urlTicket = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"

urlGen = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/"

#Credenciales
username="devnetuser"
password="Xj3BDqbU"
sTicket=""

# Funcionalidad numero 0 (prueba)
def funcionalidadN0():

    fN0Msg = " I am: " + funcionalidadN0.__name__+" "
    print(fN0Msg.center(40,"*"))
    
    vLatitude = input("Give desired LATITUDE: ")
    if vLatitude == "":
        latitude = "40.305012"
    else:
        try:
            latitude = float(vLatitude)

        except ValueError:
            print ("Wrong format...using default.")
            latitude = "40.305012"
    
    vLongitude = input("Give desired LONGITUDE: ")
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
    next_pass = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
    print("\nThe next ISS pass, over: \n    LAT: ",latitude,"\n    LONG: ",longitude,"\nWill be at: ",(next_pass))

    print("\n")
    sleep(5)
    return

# Funcionalidad numero 1
def funcionalidadN1():

    fN1Msg = " I am: " + funcionalidadN1.__name__+" "
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

# Funcionalidad numero 2    
def funcionalidadN2():

    fN2Msg = " I am: " + funcionalidadN2.__name__+" "
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

# Funcionalidad numero 3
def funcionalidadN3():

    fN3Msg = " I am: " + funcionalidadN3.__name__+" "
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
        print("\nThe", rJSON['response'][counter]['hostname'],
        "belong to ", rJSON['response'][counter]['family'],
        "family, from", rJSON['response'][counter]['type'],
        "series, with MAC",rJSON['response'][counter]['macAddress'])
        counter+=1
   
    # print("")
    sleep(3)
    return

# Funcionalidad numero 4    
def funcionalidadN4():

    fN4Msg = " I am: " + funcionalidadN4.__name__+" "
    print(fN4Msg.center(40,"*"))
    
    print("\n")
    sleep(5)
    return

def bye():
    sys.exit("Exiting...")

switcher = {
        0: funcionalidadN0,
        1: funcionalidadN1,
        2: funcionalidadN2,
        3: funcionalidadN3,
        4: funcionalidadN4,
        5: bye
    }

# El buen main...menú
def main():

    mainMsg=" MAIN MENU "

    requests.packages.urllib3.disable_warnings()

    while True:         
        print("\n",mainMsg.center(40,"*"))
        
        print ("-[1] GET TICKET 1\n-[2] GET HOSTS 2\n-[3] GET NETWORK DEVICES 3\n-[4] OPTION 4\n-[5] EXIT")
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