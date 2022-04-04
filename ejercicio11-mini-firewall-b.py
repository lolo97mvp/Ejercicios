#Cuando se detecte tres veces seguidas la misma IP se incluye en una lista negra
#Mostrar un mensaje de rechazo
ip="-1"
ip_comp="-1"
i=0
listanegra=[]
while ip!="0":
    ip=input("Introduce una dirección IP:")
    print("Estado 1")
    if ip==ip_comp:
        i+=1
        print("Estado 2")
        print("i es",i)
    else:
        ip_comp=ip
        i=0
        print("Estado 3")
        print("ip_comp es",ip_comp)
    if i==3:
        i=0
        listanegra.append(ip)
        print("Eres un impostor")
        print("Estado 4")