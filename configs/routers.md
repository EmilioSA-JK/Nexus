# Here we have all the router configurations.

## Nexus_RP
enable
config t
hostname Nexus_RP
int s0/3/0
ip address 200.100.10.1 255.255.255.252
encapsulation frame-relay
no shutdown
exit

router ospf 1
 network 192.169.10.0 0.0.0.255 area 0
 network 200.100.10.0 0.0.0.3 area 0
 exit
int S0/3/0
 ip ospf network point-to-point
 ip nat outside
 exit
int g0/0
 ip address 192.168.10.1 255.255.255.0
 no shut
 ip nat inside
 exit
access-list 1 permit 192.169.10.0 0.0.0.255



## PromesasIT_RP

enable
config t
hostname PromesasIT_RP
Int s0/3/0
ip address 200.100.10.2 255.255.255.252
encapsulation frame-relay
no shutdown
exit

router ospf 1
 network 172.16.0.0 0.0.255.255 area 0
 network 200.100.10.0 0.0.0.3 area 0
exit
int S0/3/0
 ip ospf network point-to-point
 exit
int g0/0
 ip address 172.16.10.1 255.255.0.0
 no shut



