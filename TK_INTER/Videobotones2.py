from tkinter import *
def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")
    
def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

#Creando ventana raiz
root = Tk()

#Creando variables
n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root,text="Numero 1").pack()
Entry(root,justify="center",textvariable=n1).pack()
Label(root,text="Numero 2").pack()
Entry(root,justify="center",textvariable=n2).pack()
Label(root,text="\n\nResultado").pack()
Entry(root,justify="center",textvariable=r,state="disabled").pack()

Button(root,text="Sumar",command=sumar, bd=3).pack(side="left")
Button(root,text="Restar",command=restar, bd=3).pack(side="left")
Button(root,text="Producto",command=producto, bd=3).pack(side="left")


#Creando ciclo final
root.mainloop()