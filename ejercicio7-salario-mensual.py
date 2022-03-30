#from win10toast import ToastNotifier
salarioAnual=input("Introduce el salario anual:")

if salarioAnual[1:].isnumeric()==True or salarioAnual[0]=="-":
    salarioAnual=int(salarioAnual)
    if salarioAnual>0:
        numMeses=int(input("Introduce el numero de pagas:"))
        print("Tu salario mensual es:",salarioAnual/numMeses,"€")
 #      toaster = ToastNotifier() 
 #      toaster.show_toast("Tu salario mensual es"+str(salarioAnual/numMeses))
    else:
        print ("El salario introducido no es un valor positivo")
else:
    print ("El salario introducido no es un valor numerico")



#El profesor lo realizó de otra manera para solucionar el problema
#de si se introduce como salario '-ABC' por ejemplo.