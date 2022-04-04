"""Crear dos departamentos de una empresa utilizando listas. El primer departamento
debe tener dos empleados y sus puestos y el segundo tres empleados y sus puestos.
Mostrar el segundo empleado del segundo departamento
Mostrar todos los empleados de todos los departamentos"""

empresa=[]
empleados1=["Ter Stegen","Portero"]
empleados2=["Ansu Fati","Extremo"]
empleados3=["Pardo","Central"]
empleados4=["Isi Gómez","Centrocampista"]
empleados5=["Gorka","Delantero"]

equipo1=["FC Barcelona"]
equipo2=["CD Badajoz"]

empleadosEquipo1=[empleados1,empleados2]
empleadosEquipo2=[empleados3,empleados4,empleados5]

equipo1.append(empleadosEquipo1)
equipo2.append(empleadosEquipo2)

empresa.append(equipo1)
empresa.append(equipo2)
print(empresa)
#print(empresa[2][1])                             #Mostrar segundo empleado
for departamento in empresa:
    print("DEPARTAMENTO:",departamento[0])
    for empleado in departamento[1]:
        print("--Empleado:",empleado[0])
        print("--Categoría:",empleado[1])
print("shupri",departamento[1])