lista = [3,8,10,23,0]

try:
    ind1 = int(input("Introduce el primer indice de la lista: "))
    ind2 = int(input("Introduce el segundo indice de la lista: "))
    resultado = lista[ind1] / lista[ind2]
except ValueError:
    print("El indice introducido no es numerico")
except IndexError:
    print("El indice introducido está fuera de rango")
except ZeroDivisionError:
    print("No puede realizarse division entre 0, escoja otro indice ind2")
except:                                                                     #este except siempre va al final ya que es el de mayor calibre
    print("Ha ocurrido otro error")
else:
    print("El resultado es: ",resultado)