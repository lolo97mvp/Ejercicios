animals_list = ["DOG","CAT","BIRD","COW","SNAKE"]
#animals_list = ["Dog","Cat","Bird","Cow","Snake"]
animal = input("Introduce el nombre de un animal en inglés: ")
animal = animal.upper()

while animal not in animals_list:
    print("Error","\n","No se encuentra el animal introducido")
    animal = input("Introduce el nombre de un animal en inglés: ")
    animal = animal.upper()
else:
    print("Ahora si socio, correcto")