class Route:
    def __init__(self, subnet, mask, gateway, interface, obj):
        self.subnet = subnet # Подсеть
        self.mask = mask # Маска
        self.gateway = gateway # Шлюз
        self.interface = interface # Интерфейс
        self.obj = obj

class Router:
    def __init__(self, routingTable):
        self.routingTable = routingTable # Таблица маршрутизации

class Machine:
    def __init__(self, routingTable):
         self.routingTable = routingTable # Таблица маршрутизации

class Subnet:
    def __init__(self, subnet, mask):
        self.subnet = subnet
        self.mask = mask