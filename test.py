from classes import *

subnetA = Subnet(
    subnet='192.168.10.0'
)

routerA = Router(
    [
    Route(
        subnet='192.168.100.0',
        mask='255.255.255.252',
        gateway='0.0.0.0',
        interface='2',
        obj=None
    ), 
    Route(
        subnet='192.168.10.0',
        mask='255.255.255.0',
        gateway='0.0.0.0',
        interface='1',
        obj=None
    ),
    Route(
        subnet='192.168.20.0',
        mask='255.255.255.0',
        gateway='0.0.0.0',
        interface='3',
        obj=None
    ),
    ],
    Route(
        subnet='0.0.0.0',
        mask='0.0.0.0',
        gateway='192.168.100.2',
        interface='2',
        obj=None
    )
)
