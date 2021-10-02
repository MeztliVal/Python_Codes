from tkinter import *

root = Tk()

root.title("Hola Mundo soy Meztli")
root.resizable(13,13)
frame = Frame(root, width="480", height=320)
#frame.pack(anchor="ne")
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate", bg="purple", bd=30, relief="sunken")

root.config(cursor="arrow", bg="green", relief="ridge")



#bucle final de la aplicacion
root.mainloop()