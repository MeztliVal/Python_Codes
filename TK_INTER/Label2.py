from tkinter import *
#Configuración de la raiz
root = Tk()
#Strignvars = variables dinámicas (se debe crear despues del root)
texto = StringVar()
texto.set("Un nuevo texto por stringvar")

Label(root, text ="Hola Mundo").pack(anchor="nw")
label=Label(root, text ="Otra etiqueta la 2")
label.pack(anchor="center") #al ser empacado aqui aparece en el medio de la ventana
Label(root, text ="Etiqueta #3").pack(anchor="se")


label.config(bg="green", fg="white", font=("Verdana",24)) #El atributo font recibe una tupla con 2 datos, el tipo de letra y el tamaño en pixeles
label.config(textvariable=texto)

#Bucle final
root.mainloop()

#las labels pueden contener imagenes, TKinter solo acepta imagenes
#en formato PMG y GIF