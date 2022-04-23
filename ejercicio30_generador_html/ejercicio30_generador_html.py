tupla = (("Enero",10000),("Febrero",3000),("Marzo",5000))
fichero = open("salida.html","w")

fichero.write(""" 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
    <title>Tabla de ventas</title> 
</head> 
<body> 
    <h1>Ventas anuales</h1> 
    <table> 
        <tr> 
            <td>Messi</td> 
            <td>Ventassi</td> 
        </tr>
""")
for i in range(len(tupla)):
    if i==0:
        fichero.write("<tr>")
        fichero.write("Mes / Ventas")
        fichero.write("</tr>")
    fichero.write("<tr>")
    fichero.write(f"<td>El mes {tupla[i][0]} has vendido {tupla[i][1]}" + "</td>")
    fichero.write("</tr>")

fichero.write(""" </table> 
</body> 
</html>
""")

fichero.close()
