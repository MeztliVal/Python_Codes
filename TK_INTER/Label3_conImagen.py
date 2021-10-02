from tkinter import *

#Configuración de la raiz
root = Tk()

imagen = PhotoImage(file="/home/meztli/Documentos/REPO_GIT/CODIGOS_PYTHON/TK_INTER/ardilla.gif")
Label(root, image=imagen, bd=0).pack()

#Bucle final
root.mainloop()

#las labels pueden contener imagenes, TKinter solo acepta imagenes
#en formato PMG y GIF, Si quieres usar otros formatos de imagenes
#hay que trabajar con un modulo llamado pill