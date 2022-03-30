#Programa que pida el nombre la edad y te diga si eres mayor/menor
#Forma corta
nombre=input("Dime tu nombre:")
edad=int(input("Dime tu edad:"))
if edad>=18:
    print("Hola","",nombre,". Eres mayor de edad",sep="")
else:
    print("Hola","",nombre,". Eres menor de edad",sep="")