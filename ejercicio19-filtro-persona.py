import datetime as dt
anyo_actual = dt.date.today().year

nombre_completo = input("Introduce tu nombre completo: ")
anyo_nacimiento = int(input("Introduce tu año de nacimiento: "))
email = input("Introduce tu email: ")
tlf = input("Introduce tu número de teléfono: ")

nombre_es_valido = len(nombre_completo) >= 10
anyo_es_valido = (anyo_actual - anyo_nacimiento) >= 18
email_es_valido = email.count("@") == 1
tlf_es_valido = tlf.isnumeric()
hayError = False

#Solución CUTRE
if nombre_es_valido and anyo_es_valido and email_es_valido and tlf_es_valido:
    print("Cumple")
else:
    print("No cumple")

#Solucion ACEPTABLE
if not nombre_es_valido:
    print("El nombre debe tener al menos 10 caracteres")
    hayError = True
if not anyo_es_valido:
    print("Debe ser mayor de edad")
    hayError = True
if not email_es_valido:
    print("El correo no es válido")
    hayError = True
if not tlf_es_valido:
    print("El telefono no es correcto")
    hayError = True
if not hayError:
    print("Todo correcto")
