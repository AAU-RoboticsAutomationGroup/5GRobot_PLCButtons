# author: r. p. hodgkinson
# date: 26/01/23
# title: Modbus2MQTT.py
# description: a script to poll status coils on a modbus server and publish them to an MQTT topic.

########################################### Import ##################################################

import sys
from time import sleep
#from paho.mqtt.client import client as mqtt
from pymodbus.client import ModbusTcpClient

#################################### Variable Definitions ###########################################
### Modbus TCP Client Variables
MbClient = ModbusTcpClient('192.168.1.197')
monitorRate = 1
############################################ Main ###################################################

## Connect to MODBUS Server
MbClient.connect()

##### Continue until exited #####
try:
    while True: 
##### Read MODBUS coils #####
## Read discrete inputs 0-7
        request = MbClient.read_discrete_inputs(0,8)
#response = MbClient.execute(request)
## Print response to console
        print(request.bits)
        

##### Publish to MQTT topic #####

## wait monitor rate
        sleep(monitorRate)
except KeyboardInterrupt:
## Disconnect from server
    MbClient.close()
## Close program
    sys.exit(0)