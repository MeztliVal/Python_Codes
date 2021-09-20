import tkinter as tk 

class Application():
    contador =1
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x60")
        self.window.title("Ejemplo 5")
        self.window.resizable(width=False, height=False)
        self.createButton()
        self.createLabel()
        self.window.mainloop()
        
    def createButton(self):
        self.button = tk.Button(self.window, text="Incrementa", command=self.increase)
        self.button.pack()
        
    def createLabel(self):
        self.tag = tk.Label(self.window, text=0, fg="blue")
        self.tag.pack(pady=10)
        
    def increase(self):
        self.tag["text"] = self.contador
        self.contador+=1

app = Application()