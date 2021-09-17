import tkinter as tk

def abrir():
    window2 = tk.Toplevel(window)
    window2.config(bg="pink")
    window2.geometry("220x600") #ancho, alto
    window2.title("Ventana2")
    
window = tk.Tk()
window.config(bg="blue")
window.geometry("200x150")
window.title("Ventana1")
button = tk.Button(window,text="Abrir Ventana2", command=abrir)
button.grid(row=1, column=1)
window.mainloop()