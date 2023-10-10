# 9Contador de vocales:
# Desarrolla un programa que cuente cuántas vocales hay en una cadena de texto ingresada por el usuario.
import string
print("inicio del programa")

lista = list(input("Ingrese la palabra para contar las vocales : "))
# lista = list[palabra]
contador = 0


for x in lista:
    if (
        (x) == 'a'
        or (x) == "e"
        or (x) == "i"
        or (x) == "o"
        or (x) == "u"
    ):
        contador = contador + 1
    elif (
        (x) == "A"
        or (x) == "E"
        or (x) == "I"
        or (x) == "O"
        or (x) == "U"
    ):
        contador = contador + 1

print(lista)
print("El total de vocales es de : ", contador)

print("Fin del programa")
