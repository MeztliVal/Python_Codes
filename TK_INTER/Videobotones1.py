from tkinter import *

def crear_label():
    Label(root,text="Label creada dinámicamente").pack()

#Creando ventana raiz
root=Tk()

Button(root, text="Pulsame", command=crear_label).pack()


#Creando ciclo final de app
root.mainloop()