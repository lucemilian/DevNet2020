from netmiko import ConnectHandler

#Conectamos al dispositivo
sshovercli = ConnectHandler(device_type="cisco_ios",host="192.168.56.101",port=22,username="lucemilian",password='devnet2020!')

#Varias instrucciones de linea unica, puestas como funciones
def shVersion():
    output1 = sshovercli.send_command("sh version")
    print("sh version:\n{}".format(output1))
def showRun():
    output2 = sshovercli.send_command("show run")
    print("sh version:\n{}".format(output2))

def showIPintB():
    output3 = sshovercli.send_command("show ip interface brief")
    print("show ip interface brief:\n{}".format(output3))


def createLOSSH():

    #Set de instrucciones de configuracion
    configCommands= ("int loopback1",
                    "ip address 1.2.3.4 255.255.255.0",
                    "description loopback over ssh")
    outputConfig = sshovercli.send_config_set(configCommands)
    print("Config output from device:\n{}".format(outputConfig))

    #Comprobamos que se ha realizado bien
    showIPintB()



shVersion()
showRun()
showIPintB()
createLOSSH()
