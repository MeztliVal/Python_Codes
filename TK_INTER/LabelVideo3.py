from tkinter import *
#Creando la raiz
root = Tk()
imagen=PhotoImage(file="/home/meztli/Documentos/REPO_GIT/CODIGOS_PYTHON/TK_INTER/ardilla.gif")
Label(root, image=imagen, bd=0).pack()

#Crear loop final
root.mainloop()