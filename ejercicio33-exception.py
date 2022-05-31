class NombreError(Exception):
    pass
class EdadError(Exception):
    pass
class MalGustoError(Exception):
    pass

def pedir_datos():
    global nombre, edad, color_fav
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    color_fav = input("Introduce tu color favorito: ")

def validacion(nombre,edad,color):
    if len(nombre) < 3:
        raise NombreError
    if edad < 18:
        raise EdadError
    if color_fav == "Naranja":
        raise MalGustoError

pedir_datos()
try:
    validacion(nombre, edad, color_fav)
except NombreError:
    print("El nombre es demasiado corto")
except EdadError:
    print("Eres menor de edad")
except MalGustoError:
    print("El color es feísimo")
else:
    print("Has pasado todos los filtros")