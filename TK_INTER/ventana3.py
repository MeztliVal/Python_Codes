import tkinter as tk

window = tk.Tk()
window.geometry("200x150")
button=tk.Button(window, text="Testing")
button.grid(row=1, column=1)
window.mainloop()