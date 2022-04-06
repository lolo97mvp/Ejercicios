"""Crear dos departamentos de una empresa utilizando listas. El primer departamento
debe tener dos empleados y sus puestos y el segundo tres empleados y sus puestos.
Mostrar el segundo empleado del segundo departamento
Mostrar todos los empleados de todos los departamentos"""

empresa=[]

dpto1=["FC Barcelona"]
dpto2=["CD Badajoz"]

empleado1=["Ter Stegen","Portero"]
empleado2=["Ansu Fati","Extremo"]
empleado3=["Pardo","Central"]
empleado4=["Isi Gómez","Centrocampista"]
empleado5=["Gorka","Delantero"]

empleadosDpto1=[empleado1,empleado2]
empleadosDpto2=[empleado3,empleado4,empleado5]

dpto1.append(empleadosDpto1)
dpto2.append(empleadosDpto2)

empresa.append(dpto1)
empresa.append(dpto2)
print(empresa)           

#Mostramos todos los datos de la empresa
for departamento in empresa:            #Ver apuntes de hoja 4 para entender el 'for'
    print("DEPARTAMENTO:",departamento[0])
    for empleado in departamento[1]:
        print("--Empleado:",empleado[0])
        print("--Categoría:",empleado[1])

#Buscamos la ategoria profesiona lde un empleado
nombre_a_buscar=input("Introduce el nombre del empleado:")
for departamento in empresa:
    for empleado in departamento[1]:
        if empleado[0]==nombre_a_buscar:
            print(empleado[0],"juega de",empleado[1],"en el club",departamento[0])