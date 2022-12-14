from classes import *
from functions import *

# Test inf
routerA = Router([Route(
    subnet='192.168.100.0',
    mask='255.255.255.252',
    gateway='0.0.0.0',
    interface='2'
    obj = ''
    )]
)

machineA = Machine(
    route = Route(
        subnet='192.168.10.0'
        mask=''
    )
    ip = '192.168.10.5'
)