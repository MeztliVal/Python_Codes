from tkinter import *
#Importante que la función este declarada antes de asignarla
def hola():
    print("Hola Mundo")

#Creando la raiz
root = Tk()

Button(root, text="Puchame", command=hola).pack()

#Bucle final de la aplicación
root.mainloop()