"""Mostramos lista y pedimos planeta.
Si acierta: indicamos uantos ntetntos ha ralizaod.
Si no acierta, se borra el planeta de la lista, se muestra la lista y se vulve a intentar"""

import random 
lista = ["Mercurio","Venus","Marte","Jupiter","Saturno","Urano","Neptuno","Pluton"] 
planeta_secreto = random.choice(lista)
planeta = input("Introduce un planeta: ")
intento = 1                                   #Por si acierta a la primera

while planeta not in lista:                 #Tb se podria hacer con n try-except, ¿cual es mejor opcion?
    planeta = input("Error. Introduce un planeta correcto: ")

while planeta != planeta_secreto:
    print("Error. El planeta no es correcto")
    intento = intento + 1
    indice = lista.index(planeta)
    del lista[indice]
    print(lista)
    planeta = input("Intentelo de nuevo. Introduce un planeta: ")
    while planeta not in lista:
        planeta = input("Error. Introduce un planeta correcto: ")
else:
    print("¡Enhorabuena, el planeta es corecto!")
    print("Numero de intentos realizados: ",intento)