from tkinter import *
#Creando ventana raiz
root = Tk()
frame1=Frame(root)
frame1.pack()

entry = Entry(frame1)
entry.pack(side="right")

label = Label(frame1, text="Nombre aún mas largo")
label.pack(side="left")

frame2= Frame(root)
frame2.pack()

entry2 = Entry(frame2)
entry2.pack(side="right")

label2 = Label(frame2, text="Apellidos")
label2.pack(side="left")

#Creando ciclo principal
root.mainloop()