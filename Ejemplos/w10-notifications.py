#pip install win10toast --> Esto y se ejecutó desde la consola una vez por lo que ya no hace falta
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Hola Lolo","Python is awesome")

#NOTA: revisar que las notificaciones están activadas en "Notificaciones y acciones" y en "Asistente de concentracion" de Windows