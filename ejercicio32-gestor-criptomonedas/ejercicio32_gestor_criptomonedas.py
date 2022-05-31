LIMITE_RENTABILIDAD = 0
NOMBRE_FICHERO = "cotizacion.dat"
def get_cotizaciones(nombre_fichero):
    criptomonedas = []
    with open("cotizacion.dat","r") as fichero:         #Cuando abres un fichero con with se cierra solo, no hace falta el close
        moneda = fichero.readline()
        while moneda!="":
            moneda = moneda.replace("\n","")
            sigla = fichero.readline().replace("\n","")
            cotizacion = float(fichero.readline().replace("\n",""))
            criptomonedas.append((moneda,sigla,cotizacion))
            moneda = fichero.readline()
    return criptomonedas

criptomonedas = get_cotizaciones(NOMBRE_FICHERO)
salida = open("salida.txt","w")
for criptomoneda in criptomonedas:          #Lo suyo es hacer una funcion de cuales hay que vender, pero sin mostrar el mensaje ya que en un futuro no sabré si querré mostrar mensaje o no
        print(f"La moneda {criptomoneda[0]} con sigla {criptomoneda[1]} tiene una cotización de {criptomoneda[2]}")
        if  criptomoneda[2] < LIMITE_RENTABILIDAD:
            print(f"Hay que vender la moneda {criptomoneda[0]}")
            #salida = open("salida.txt","w")
            salida.write(f"Hay que vender la moneda {criptomoneda[0]}" + "\n")
            salida.write("\n")
            #salida.close()
salida.close()
