class route:
    def __init__(self, subnet, net, gateway, interface):
        self.subnet = subnet
        self.net = net
        self.gateway = gateway
        self.interface = interface

class router:
    def __init__(self, routingTable):
        self.routingTable = routingTable


        