from classes import *

router1 = Router([
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
    Route(
        subnet='0.0.0.0',
        mask='0.0.0.0',
        gateway='192.168.100.2',
        interface='2',
        obj=None
    )
])

router2 = Router([
    Route(
        subnet='192.168.100.0',
        mask='255.255.255.252',
        gateway='0.0.0.0',
        interface='2',
        obj=None
    ),
    Route(
        subnet='192.168.32.0',
        mask='255.255.240.0',
        gateway='0.0.0.0',
        interface='1',
        obj=None
    ),
    Route(
        subnet='0.0.0.0',
        mask='0.0.0.0',
        gateway='192.168.100.1',
        interface='2',
        obj=None
    )
])

machineA = Machine([
    Route(
        subnet='192.168.10.0',
        mask='255.255.255.0',
        gateway='def',
        interface='def',
        obj=None
    )
])

machineB = Machine([
    Route(
        subnet='192.168.20.0',
        mask='255.255.255.0',
        gateway='def',
        interface='def',
        obj=None
    )
])

machineC = Machine([
    Route(
        subnet='192.168.32.0',
        mask='255.255.240.0',
        gateway='def',
        interface='def',
        
    )
])


# subnetA = Subnet(
#     subnet='192.168.10.0',
#     mask='255.255.255.0'
# )

# subnetB = Subnet(
    # subnet='192.168.20.0',
    # mask='255.255.255.0'
# )

# subnetC = Subnet(
    # subnet='192.168.32.0',
    # mask='255.255.240.0'
# )