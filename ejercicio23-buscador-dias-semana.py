dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
dia = input("Introduce un día de la semana: ")
i = 0

for i in dias:
    if dia == i:
        print("Correcto, es el",i)
        break
    else:
        print("Incorrecto, no es el",i)
