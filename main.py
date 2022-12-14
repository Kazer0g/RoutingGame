from classes import *
from functions import *

# Test inf
routerA = Router([
    Route(
        subnet='192.168.100.0',
        mask='255.255.255.0',
        gateway='0.0.0.0',
        interface='1'
    ), 
    Route(
        subnet='192.168.10.0',
        mask='255.255.255.0',
        gateway='0.0.0.0',
        interface='3'
    )
])

subnetA = Subnet(
    subnet='192.168.10.0',
    mask='255.255.255.0'
)
subnetB = Subnet(
    subnet='192.168.10.0',
    mask='255.255.255.0'
)



