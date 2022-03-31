EDADM=18
edad=int(input("Introduce tu edad:"))
nacionalidad=input("Introduce tu nacionalidad:")
idioma1=input("Primer idioma hablado:")
idioma2=input("Segundo idioma hablado:")
if (edad>=EDADM):
    if (nacionalidad=="Frances" or nacionalidad=="Aleman"):
        if (idioma1=="Ingles" and idioma2=="Chino"):
            print("Estás contratado, enhorabuena")
        else:
            print("Lo sentimos")
    else:
        print("Lo sentimos")
else:
        print("Lo sentimos")

#Otra manera de resolverlo
mayor_edad=edad>=EDADM
nacionalidad_ok=(nacionalidad=="Frances" or nacionalidad=="Aleman") and nacionalidad!="Ruso"
idiomas_ok=idioma1=="Ingles" and idioma2=="Chino"

if (mayor_edad and nacionalidad_ok and idiomas_ok):
    print("Estás contratado, enhorabuena")
else:
    print("Lo sentimos")