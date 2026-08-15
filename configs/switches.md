# Here we have all the switching

## Spoke Switch
en
config t
hostname Spoke_Switch
vlan 10
name CLIENTS
vlan 20
name IOT
vlan 30
name DMZ
interface fa0/1
switchport mode access
switchport access vlan 10
interface fa0/3
switchport mode access
switchport access vlan 20
interface fa0/2
switchport mode access
switchport access vlan 20
int g0/1
switchport mode trunk
switchport trunk allowed vlan 10,20,30
exit

## CLIENTS_Switch
en
config t
hostname CLIENT_Switch
vlan 10
 CLIENTS
int fa0/1
 switchport mode access 
 switchport access vlan 10
int fa0/2
 switchport mode access 
 switchport access vlan 10
int fa0/3
 switchport mode access 
 switchport access vlan 10

## DMZ_Switch
en
conf t
hostname DMZ_Switch
vlan 30
 name DMZ
int fa0/1
 switchport mode access
 switchport access vlan 30
int fa0/2
 switchport mode access
 switchport access vlan 30
int fa0/3
 switchport mode access
 switchport access vlan 30
int fa0/4
 switchport mode access
 switchport access vlan 30
int fa0/5
 switchport mode access
 switchport access vlan 30
int fa0/6
 switchport mode access
 switchport access vlan 30
 exit

 

