frase=input("Introduce una frase:")
frase=frase.upper()
texto=input("Introduce un texto a buscar:")
texto=texto.upper()
print(frase)
num=frase.count(texto)
print("El texto a buscar ha aparecido",num,"veces")