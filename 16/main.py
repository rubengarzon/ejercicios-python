# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

from tkinter import *
ventana = Tk()

elemento = StringVar()

listbox = Listbox(ventana)

for item in ["Ronaldo", "Romario", "Ronaldinho", "Roberto Carlos", "Raul", "Messi"]:
    listbox.insert(END, item)

listbox.pack()

label = Label(text="Lista de futbolistas")
label.pack()

ventana.mainloop()
