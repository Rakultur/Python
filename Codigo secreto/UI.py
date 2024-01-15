# Liebrerias
from tkinter import *
from logica import *
from tkinter import messagebox as MessageBox

# Se crea un objeto de la libreria tkinter
root = Tk()
lt = []

# Configuracion ventana aplicacion
root.geometry("800x800+400+0")
root.resizable(width=False, height=False)
root.title(" CONDIFICADOR ")
root.config(bg="#d2d4ea")


# Funciones
def cifrar():
    try:
        print(len(lt))
        lt.clear()
        lt.append(tbox.get("0.1", END))
        lt.append(codificar.cifrar(lt[0]))
        tbox_2["text"] = lt[1]
        del lt [:]
        print(len(lt))
    except:
        MessageBox.showinfo("Error", "Operación no valida")


def decifrar():
    return 0


def copiar():
    return 0


def borrar():
    tbox_2.config(text="")


# Titulo de bievenida
titulo = Label(root)
titulo.config(
    bg="#d2d4ea",
    text="Bienvenido DEVP",
    font=("arial", 30, "bold"),
)


# Cajas de texto
tbox = Text(root)
tbox.config(bg="#f0f2f0", height=13)

# Label
tbox_2 = Label(root)
tbox_2.config(bg="#f0f2f0", width=80, height=13)


# Botones
btn_1 = Button(root)
btn_1.config(border=10, text="Cifrar", bg="#e5e5e5", bd=2, command=cifrar)

btn_2 = Button(root)
btn_2.config(border=10, text="Decifrar", bg="#e5e5e5", bd=2, command=decifrar)

btn_3 = Button(root)
btn_3.config(border=10, text="copiar", bg="#e5e5e5", bd=2, command=copiar)

btn_4 = Button(root)
btn_4.config(border=10, text="borrar", bg="#e5e5e5", bd=2, command=borrar)

btn_5 = Button(root)
btn_5.config(border=10, text="Salir", bg="#e5e5e5", bd=2, command=quit)

# Metodo pack()
titulo.pack(pady=10)
tbox.pack(pady=5)
tbox_2.pack(pady=5)
btn_1.pack(pady=2)
btn_2.pack(pady=2)
btn_3.pack(pady=2)
btn_4.pack(pady=2)
btn_5.pack(pady=2)

root.mainloop()
