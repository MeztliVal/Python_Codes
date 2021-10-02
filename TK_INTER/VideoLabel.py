from tkinter import *
#Configuración de la ventana raiz
root = Tk()

label = Label(root, text="Hola Mundo soy Meztli")
label.pack()
Label(root, text="Otra Etiqueta - #2").pack(anchor="ne")
Label(root, text="Esta es la etiqueta #3").pack(anchor="sw")

label.config(bg="green", fg="white", font=("Verdana",24))

#Bucle final
root.mainloop()