# Interfaz grafica de inicio
#  python -m tkinter // Comando para saber si la herramiento de TK esta instalada en el ordenador

from tkinter import *

# Objeto de tk
root = Tk()
root.title("UI")

# Ventana obj 1
ventana = Frame()
ventana.config(width="500", height="500")
ventana.config(background="#855555")

# Ventana obj 2 y 3 
txt_1 = Label(root, text="¡Bienvenido!")
txt_2 = Label(root, text="¡Usuario¡")

# Posicion grid
ventana.grid(row=0, column=0)
txt_1.grid(row=1, column=1)
txt_2.grid(row=2, column=2)

root.mainloop()