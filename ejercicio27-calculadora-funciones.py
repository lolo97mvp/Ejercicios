operacion = -1
def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")

def suma(s1,s2):
    resultado = s1 + s2
    return resultado

def resta(r1,r2):
    resultado = r1 - r2
    return resultado

def multiplicacion(m1,m2):
    resultado = m1 * m2
    return resultado

def division(d1,d2):
    resultado = d1 / d2
    return resultado

def gestionar_operaciones(operacion,n1,n2):
    if operacion == 1:
        resultado = suma(n1,n2)
    if operacion == 2:
        resultado = resta(n1,n2)
    if operacion == 3:
        resultado = multiplicacion(n1,n2)
    if operacion == 4:
        resultado = division(n1,n2)
    return resultado

while operacion != 0:
    mostrar_menu()
    try:
        operacion = int(input("Introduce la operación a realizar (0-4): "))
        if operacion in (1,2,3,4):
            n1 = int(input("Introduce el primer número: "))
            n2 = int(input("Introduce el segundo número: "))
            resultado = gestionar_operaciones(operacion,n1,n2)
            print("El resultado es: ",resultado)
    except:
        print("Ha ocurrido un error")

print("Fin de la calculadora")
        