personas = [["Fernando", 1971], 
["Francisco", 1988], 
["Javier", 1990], 
["Juanjo", 1973], 
["Federica", 1999]]

letra = input("Introduce la primera letra del nombre: ")
año = int(input("Introduce el año de nacimiento: "))

for persona in personas:
    if (persona[0][0]==letra):
        print(persona[0])