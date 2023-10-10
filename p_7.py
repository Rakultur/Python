# 7 Generador de contraseñas:
# Crea un generador de contraseñas que genere contraseñas seguras con letras, números y símbolos aleatorios.

import random
import string

print("Inicio del programa")

tamaño = int(input("Por favor ingrese el tamaño de la contraseña"))
lista = []

for x in range(tamaño):
    lista.append(
        random.choice(
            string.ascii_letters
            + string.digits
            + string.punctuation
            + string.ascii_uppercase
        )
    )
print("Su contraseña generada es : ")
for n in range(len(lista)):
    print (lista[n], end="")

print("\n Fin del programa")