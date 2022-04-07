#CALCULA EL IMC = PESO / (ALTURA)^2  (kg/m^2)
import winsound                 #Es un extra, con esta instruccion importamos la librería para emitir el sonido
LIM_DELG_MUYSEV=15
LIM_DELG_SEV=16
LIM_DELG=18.5
LIM_SALUDABLE=25
LIM_SOBR=30
LIM_OBES_MOD=35
LIM_OBES_SEV=40

peso=int(input("Introduce tu peso en kg:"))
altura=float(input("Introduce tu altura en m:"))
imc=peso/altura**2

if imc <= LIM_DELG_MUYSEV:
    estado=("DELGADEZ MUY SEVERA")
elif imc > LIM_DELG_MUYSEV and imc < LIM_DELG_SEV:
    estado=("DELGADEZ SEVERA")
elif imc >= LIM_DELG_SEV and imc < LIM_DELG:
    estado=("DELGADEZ")
elif imc >= LIM_DELG and imc < LIM_SALUDABLE:
    estado=("PESO SALUDABLE")
elif imc >= LIM_SALUDABLE and imc < LIM_SOBR:
    estado=("SOBREPESO")
elif imc >= LIM_SOBR and imc < LIM_OBES_MOD:
    estado=("OBESIDAD MODERADA")
elif imc >= LIM_OBES_MOD and imc < LIM_OBES_SEV:
    estado=("OBESIDAD SEVERA")
else:
    estado=("OBESIDAD  MUY SEVERA")
print("%.2f" % imc)               #Así se hace el redondeo
print("Tu IMC es:",estado)
winsound.Beep(int(imc),1000)      #Es un extra, con esta instruccion el ordenador emite un sonido