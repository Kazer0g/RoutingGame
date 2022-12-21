from classes import *

routers = [
    Router([
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
    ]),

    Router([
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
]

# machines = [
    # Machine([
    #     Route(
    #         subnet='192.168.10.0',
    #         mask='255.255.255.0',
    #         gateway='def',
    #         interface='def',
    #         obj=None
    #     )
    # ]),

    # Machine([
    #     Route(
    #         subnet='192.168.20.0',
    #         mask='255.255.255.0',
    #         gateway='def',
    #         interface='def',
    #         obj=None
    #     )
    # ]),

    # Machine([
    #     Route(
    #         subnet='192.168.32.0',
    #         mask='255.255.240.0',
    #         gateway='def',
    #         interface='def',
    #         obj=None
    #     )
    # ])
# ]

subnets = [
    Subnet([
        Route(
            subnet='192.168.10.0',
            mask='255.255.255.0',
            gateway='def',
            interface='def',
            obj=None
        )
    ]),

    Subnet([
        Route(
            subnet='192.168.20.0',
            mask='255.255.255.0',
            gateway='def',
            interface='def',
            obj=None
        )
    ]),

    Subnet([
        Route(
            subnet='192.168.32.0',
            mask='255.255.240.0',
            gateway='def',
            interface='def',
            obj=None
        )
    ])
]
