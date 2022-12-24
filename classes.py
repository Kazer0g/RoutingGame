class Package:
    def __init__(self, recipientIp):
        self.recipientIp = recipientIp

class Subnet:
    def __init__(self, objects):
       self.objects = objects

    def take_package(self, package):
        for object in self.objects:
            object.take_package(package) 

class Machine:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def take_package(self):
        print('Hi')

    def send_package(self, package):
        self.subnet.take_package(package)


class Router:
    def __init__(self, routingTable, defaultRoute, interfaces):
        self.roitingTable = routingTable
        self.defaultRoute = defaultRoute
        self.interfaces = interfaces

    # def take_package(self, package):
    #     for route in self.roitingTable:
