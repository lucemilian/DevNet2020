from ncclient import manager
import xml.dom.minidom

#Definimos conexión
con = manager.connect(host="192.168.56.101",port=830,username="lucemilian",password='devnet2020!',hostkey_verify=False)

def giveALL():
    #Recoger información del dispositivo
    netconf_reply = con.get_config(source="running")

    #Configuración de impresión
    # print(netconf_reply)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def filterNC():
    #Filtro para netconf
    netconf_filter = """ 
    <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
    </filter> """

    netconf_reply = con.get_config(source="running", filter=netconf_filter)

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



def configNChost():
    #Cofing para cambiar hostname de CSR1kv a MyCSR1000v
    netconf_host = """ 
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>MyCSR1000v</hostname>
        </native> 
    </config>
    """

    netconf_reply = con.edit_config(target="running", config=netconf_host)

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


def configNCinterface():
    #Cofing para cambiar hostname de CSR1kv a MyCSR1000v
    netconf_interface= """ 
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                        <name>88</name>
                        <description>TestLoop 88</description>
                        <ip>
                            <address>
                                <primary>
                                        <address>88.88.88.88</address>
                                        <mask>255.255.255.0</mask>
                                </primary>
                            </address>
                        </ip>
                </Loopback>
            </interface>
        </native> 
    </config>
    """

    netconf_reply = con.edit_config(target="running", config=netconf_interface)

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



# giveALL()
# filterNC()
# configNChost()
# configNCinterface()