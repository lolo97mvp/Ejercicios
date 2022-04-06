vehiculo1=["Kia","Sportage","Blanco"]
vehiculo2=["Skoda","Fabia","Rojo"]
vehiculo3=["Renault","Megane","Azul"]

coches={"1234":vehiculo1,"4567":vehiculo2,"8901":vehiculo3}
matricula=input("Introduce la amtrícula abuscar:")

"""#SOLUCION 2
vehiculo_buscado=coches.get(matricula)
if vehiculo_buscado==None:
    print("La matricula no existe")
else:
    print(vehiculo_buscado)
"""

#SOLUCION 1
if matricula in coches:
    print(coches[matricula])
else:
    print("La matricula no existe")


""" #SOLUCION TRY EXCEPT - CONTROL DE ERRORES
try:
    vehiculo_buscado=coches[matricula]
    print(vehiculo_buscado)
except:
    print("El vehiculo no existe")
"""