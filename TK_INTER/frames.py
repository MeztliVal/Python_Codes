from tkinter import *
root = Tk()
root.title("Hola Mundo soy Meztli")
root.resizable(13,13)
frame = Frame(root, width=480, height=320)
#frame.pack(side="bottom", anchor="w")
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate", bg='lightblue', bd=25, relief="sunken")

root.config(cursor="arrow", bg='blue', bd=15, relief="ridge")

#Bucle de la aplicación
root.mainloop()