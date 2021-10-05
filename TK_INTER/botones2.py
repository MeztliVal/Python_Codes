from tkinter import *
#Importante que la función este declarada antes de asignarla
def hola():
    print("Hola Mundo")

def crear_label():
    Label(root, text="Label creada dinamicamente").pack()
    
#Creando la raiz
root = Tk()

Button(root, text="Puchame", command=crear_label).pack()

#Bucle final de la aplicación
root.mainloop()