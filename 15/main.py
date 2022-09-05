# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

from tkinter import *

# crear la ventana
ventana = Tk()
ventana.title("Ejercicio 15")
ventana.geometry("200x200")

# crear la variable de los radiobutton
var = StringVar()
var.set(None)

# crear los radiobutton
radio1 = Radiobutton(ventana, text="Opción 1", variable=var, value="Opción 1")
radio2 = Radiobutton(ventana, text="Opción 2", variable=var, value="Opción 2")
radio3 = Radiobutton(ventana, text="Opción 3", variable=var, value="Opción 3")

# mostrar los radiobutton
radio1.pack()
radio2.pack()
radio3.pack()

# crear label para mostrar la opción seleccionada
label = Label(ventana, textvariable=var)
label.pack()

# crear boton para reiniciar

Button(ventana, text="Reiniciar", command=lambda: var.set(None)).pack()


ventana.mainloop()
