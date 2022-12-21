from classes import *
from functions import *
from first import *

etherinit(routers, subnets)

for router in routers:
    for route in router.routingTable:
        print (route.subnet)
        try:
            subnet = route.obj
            print (subnet.subnet)
        except:
            pass