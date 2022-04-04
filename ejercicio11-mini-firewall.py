#Cuando se detecte tres veces la misma IP se incluye en una lista negra
#Mostrar un mensaje de rechazo

NUMERO_INTENTOS=3
IP_SALIDA=0
ip="-1"
listaIP=[]
listanegra=[]
while ip!=IP_SALIDA:
    ip=input("Introduce una dirección IP:")
    if ip in listanegra:    #Esto interesa ponerlo como primer if, ya que es lo más restrictivo
        print(listanegra)
        print("Eres un impostor")
    else:
        listaIP.append(ip)
        print(listaIP)
        if listaIP.count(ip)==NUMERO_INTENTOS:
            listanegra.append(ip)