class Route:
    def __init__(self, subnet, mask, gateway, interface, obj):
        self.subnet = subnet # Подсеть
        self.mask = mask # Маска
        self.gateway = gateway # Шлюз
        self.interface = interface # Интерфейс
        self.obj = obj

class Router:
    def __init__(self, routingTable, defaultRoute):
        self.routingTable = routingTable # Таблица маршрутизации
        self.defaultRoute = defaultRoute

    # def etherinit (self, )

    def nextstep (self, recipient):
        for route in self.routingTable:
            if route.subnet == recipient.subnet:
                return route.obj
        return self.defaultRoute.obj
                 
            

# class Machine:
#     def __init__(self, routingTable):
#          self.routingTable = routingTable # Таблица маршрутизации

class Subnet:
    def __init__(self, subnet):
        self.subnet = subnet
        # self.routingTable = routingTable
        # self.subnet = subnet
        # self.mask = mask