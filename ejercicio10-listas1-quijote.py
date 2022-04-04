import urllib.request
webUrl = urllib.request.urlopen('https://www.gutenberg.org/files/2000/2000-0.txt')
data = webUrl.read()
data=str(data)  #Convertimos los bytes recibidos en un string
data=data.upper()
data=data.split()
palabra=input("Introduce la palabra a buscar:")
palabra=palabra.upper()
print("La palabra",palabra,"aparece",data.count(palabra),"veces")
if palabra in data:
    print("La palabra aparece en el texto")
else:
    print("La palabra no aparece en el texto")