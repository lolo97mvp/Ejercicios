PALABRA_PROHIBIDA1="ADMIN"
PALABRA_PROHIBIDA2="123"
PALABRA_PROHIBIDA3="PASSWORD"

id=input("Introduce el nombre de usuario:")
pwd=input("Introduce la contraseña:")


#Resolución con 'count'. Hay que comentar los metodos excepto el que queremos que funcione
if pwd.count(PALABRA_PROHIBIDA1)==0:
    if pwd.count(PALABRA_PROHIBIDA2)==0:
        if pwd.count(PALABRA_PROHIBIDA3)==0:
            print("contraseña correcta")
        else:
            print("error")
    else:
        print("error")
else:
    print("error")

#Resolución con 'in'. Hay que comentar los metodos excepto el que queremos que funcione
if PALABRA_PROHIBIDA1 in pwd:
    print("Error")
elif PALABRA_PROHIBIDA2 in pwd:
    print("Error")
elif PALABRA_PROHIBIDA3 in pwd:
    print("Error")
else:
    print("Correcta")
