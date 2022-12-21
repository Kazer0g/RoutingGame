# Проверяет длину бинарной записи (== 8)
def octanlen (octan):
    return ('0'*(8-len(octan))+octan)

# Конвертирует бинарную запись в IP-адрес строку
def binstringtoipstring (binstring):
    l = binstring.split('.')
    l = [str(int('0b'+i, 2)) for i in l]
    IPstring = (
        l[0]+'.'+
        l[1]+'.'+
        l[2]+'.'+
        l[3]
        )
    return IPstring

# Конвертирует IP-адрес строку в бинарную запись 
def ipstringtobinstring (ipstring):
    l = ipstring.split('.')
    l = [bin(int(i))[2:] for i in l]
    binstring = (
        octanlen(l[0])+'.'+
        octanlen(l[1])+'.'+
        octanlen(l[2])+'.'+
        octanlen(l[3])
        )
    return binstring

# Устанавлиевает "Ethernet" соединение между объектами
def etherinit (routers, subnets):
    for router in routers: # Роутер из списка
        for route in router.routingTable: # Маршрут из таблицы роутера
            for subnet in subnets: # Перебор подсетей
                print (subnet.routingTable[0].subnet)
                if subnet.routingTable[0].subnet == route.subnet: 
                    route.obj = subnet # Спопоставление IP-подсетей
                    subnet.routingTable[0] = router
            

# def way (current, recipient):
    
