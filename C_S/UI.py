# Liebrerias
from tkinter import *
from customtkinter import *
from logica import *
from tkinter import messagebox as MessageBox

# Se crea un objeto de la libreria tkinter
root = CTk()
lt = []

# Configuracion ventana aplicacion
root.geometry("800x800+400+0")
root.resizable(width=False, height=False)
root.title(" CONDIFICADOR ")
root.config(bg="#d2d4ea")


# Funciones
def cifrar():
    try:
        tbox_2.delete(1.0, END)
        lt.clear()
        lt.append(tbox.get("0.1", END))
        lt.append(codificar.cifrar(lt[0]))
        tbox_2.insert(1.0, lt[1])
        del lt[:]
    except:
        MessageBox.showinfo("Error", "Operación no valida")


def decifrar():
    try:
        tbox_2.delete(1.0, END)
        lt.clear()
        lt.append(tbox.get("0.1", END))
        lt.append(codificar.decifrar(lt[0]))
        tbox_2.insert(1.0, lt[1])
        del lt[:]
    except:
        MessageBox.showinfo("Error", "Operación no valida")


def borrar():
    tbox_2.delete(1.0, END)


# Configuracion entornos
titulo = Label(root)
titulo.config(
    bg="#d2d4ea",
    text="Bienvenido DEVP",
    font=("arial", 30, "bold"),
)

tbox = Text(root)
tbox.config(bg="#f0f2f0", height=13)

tbox_2 = Text(root)
tbox_2.config(bg="#f0f2f0", height=13)

btn_1 = Button(root)
btn_1.config(
    border=10, text="Cifrar", bg="#e5e5e5", width="10", height="2", bd=2, command=cifrar
)

btn_2 = Button(root)
btn_2.config(
    border=10,
    text="Decifrar",
    bg="#e5e5e5",
    width="10",
    height="2",
    bd=2,
    command=decifrar,
)

btn_4 = Button(root)
btn_4.config(
    border=10, text="borrar", bg="#e5e5e5", width="10", height="2", bd=2, command=borrar
)

btn_5 = Button(root)
btn_5.config(
    border=10, text="Salir", bg="#e5e5e5", width="10", height="2", bd=2, command=quit
)

# pack()
titulo.pack(pady=10)
tbox.pack(pady=5)
tbox_2.pack(pady=5)
btn_1.pack(pady=6)
btn_2.pack(pady=6)
btn_4.pack(pady=6)
btn_5.pack(pady=6)

root.mainloop()
