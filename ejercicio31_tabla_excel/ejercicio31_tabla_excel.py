#VER SOLUCIÓN DEL PROFESOR

dias_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes")
ventas_S1 = ["2083","10","-283","2023","10"]
ventas_S2 = [38,183,19,11,18]

fichero = open("salida_excel.csv","w")
fichero.write("VENTAS".center(50))
fichero.write("\n")
for i in range(len(dias_semana)):
    fichero.write(dias_semana[i].ljust(10) + ";")
fichero.write("\n")
for i in range(len(dias_semana)):
    fichero.write(ventas_S1[i].ljust(10) + ";")
fichero.write("\n")
for i in range(len(dias_semana)):
    fichero.write(str(ventas_S2[i]).ljust(10) + ";")

fichero.close()