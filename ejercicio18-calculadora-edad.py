import datetime as dt
anyo_actual = dt.date.today().year
anyo_nacimiento = int(input("Introduce tu año de nacimiento: "))
edad = anyo_actual - anyo_nacimiento

if edad >= 65:
    franja = "Eres jubilado"
elif edad >= 40:
    franja = "Eres adulto"
elif edad >= 18:
    franja = "Eres mayor de edad"
else:
    franja = "Eres menor de edad"
print(franja)