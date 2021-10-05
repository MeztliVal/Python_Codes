from tkinter import *

#Configuración de la raiz
root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar() #1 si, 0 no
azucar = IntVar() #1 si, 0 no

imagen = PhotoImage(file="/home/meztli/Documentos/REPO_GIT/CODIGOS_PYTHON/TK_INTER/cafe.gif")
Label(root,image=imagen).pack(side="left")

Label(root, text="¿Como quieres el cafe?").pack()
Checkbutton(root,text="Con leche",variable=leche, onvalue=1, offvalue=0).pack()
Checkbutton(root,text="Con azucar",variable=azucar, onvalue=1, offvalue=0).pack()



#Ciclo final de la aplicación
root.mainloop()