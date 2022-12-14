class Route:
    def __init__(self, subnet, mask, gateway, interface, obj):
        self.subnet = subnet # Подсеть
        self.mask = mask # Маска
        self.gateway = gateway # Шлюз
        self.interface = interface # Интерфейс

class Router:
    def __init__(self, routingTable):
        self.routingTable = routingTable # Таблица маршрутизации

class Machine:
    def __init__(self, ip, route): 
        self.ip = ip # IP-машины
        
class Data:
    def __init__(self, sender, recipient, currentplace):
        self.sender = sender
        self.recipient = recipient
        self.currentplace = currentplace