import generador_cosas_random as gcr
NUM_PERS_PWD = 100
fichero = open("salida.csv","w")

persona = gcr.generar_listado_personas(NUM_PERS_PWD)
fichero.write("PERSONAS" + ";" + "CONTRASEÑAS" + "\n")
for i in range(NUM_PERS_PWD):
    pwd = gcr.generar_contrasenya(10)
    fichero.write(persona[i] + ";" + pwd + "\n")

fichero.close()