# Adivina el número:
# Crea un juego en el que la computadora elija un número aleatorio entre 1 y 100, y el usuario debe adivinarlo. 
# Proporciona pistas como "más alto" o "más bajo" hasta que el usuario adivine el número.

import random

print("Inicio de programa")

ganador = int(random.uniform(0,100))
indicador = True
intentos = 1

while indicador == True:
    numero = int(input("Ingrese el numero : "))
    if numero == ganador:
        print("Ganaste!")
        indicador = False
    elif numero != ganador :
        intentos = intentos+1
        if numero < ganador :
            print("El numero es mayor!")
        else :
            print("El numero es menor!")


print("Tu numero de intentos fue de  : " , intentos)

print("Fin del programa")