class Route:
    def __init__(self, subnet, mask, gateway, interface, obj):
        self.subnet = subnet # Подсеть
        self.mask = mask # Маска
        self.gateway = gateway # Шлюз
        self.interface = interface # Интерфейс

class Router:
    def __init__(self, routingTable):
        self.routingTable = routingTable # Таблица маршрутизации

