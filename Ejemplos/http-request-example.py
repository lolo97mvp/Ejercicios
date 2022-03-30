import urllib.request
webUrl = urllib.request.urlopen('https://www.as.com')
data = webUrl.read()
data=str(data)  #Convertimos los bytes recibidos en un string
print(type(data))
print(data.count("Barcelona")

#Esto podría servir para por ejemplo en una pagina de ofertas de empleo ver cuantas veces aparece la palabra python por ejemplo,
# o que se ejecute automaticamente y poner una alarma para ver cuando aparece x palabra