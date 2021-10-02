from tkinter import *
root = Tk()
#Stringvars son variables dinamicas que se deben crear despues del root
texto = StringVar()
texto.set("Un nuevo texto por StringVar")

label = Label(root, text="Otra Etiqueta")
label.config(bg="purple",fg="white",font=("Verdana",20))
label.config(textvariable=texto)
label.pack()

#Bucle final
root.mainloop()