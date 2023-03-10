# 5GRobot_PLCButtons

The following are links to the Beckhoff componenets for the Remote IO unit in use for IO functionality
for the 5G robot project.

RemoteIO unit >> https://www.beckhoff.com/da-dk/products/i-o/bus-terminals/bkxxxx-bus-coupler/bk9050.html

RemoteIO>Slot1 >> https://www.beckhoff.com/da-dk/products/i-o/bus-terminals/kl2xxx-digital-output/kl2794.html
RemoteIO>Slot2 >> https://www.beckhoff.com/da-dk/products/i-o/bus-terminals/kl1xxx-digital-input/kl1408.html
RemoteIO>Slot3 >> https://www.beckhoff.com/da-dk/products/i-o/bus-terminals/kl2xxx-digital-output/kl2622.html
RemoteIO>Slot4 >> https://www.beckhoff.com/da-dk/products/i-o/bus-terminals/kl9xxx-system/kl9010.html

The status of the buttons can be read from the Remote IO unit's MODBUS registers with the folowing command:

modpoll -t 1 -c 8 192.168.1.197

Where;    <ul><li>modpoll is a freeware MODBUS master simulator, available here - https://www.modbusdriver.com/modpoll.html</li>
          <li>-t 1  refers to the MODBUS Function Code, in this case FC2. Alternatives are documented. </li>
          <li>-c 8  refers to the number of coils (or registers) to read. Default is 1 </li>
          <li>192.168.1.197 is the IP-Address, the unit is currently DHCP-enabled. This information has the additional  
              effect of indicating a normal MODBUS/TCP connection - i.e. port 502 - although alterations to the norm  
              can be specified.</li></ul>  
              
Currently, the connector is directly through polling the MODBUS registers. This will be carried out wirelessly by the AGV PLC untill  
Intelligent Systems can provide a replacement.
