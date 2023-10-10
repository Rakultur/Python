# 10Piedra, papel o tijeras:
# Implementa el juego clásico "piedra, papel o tijeras" en Python. El usuario y la computadora deben elegir una opción,
# y luego se determina quién gana según las reglas del juego

from random import choice

print("Inicio del juego")

jugador = int(input("1. Piedra\n2. Papel\n3. Tijeras\n"))
computadora = int(choice([1, 2, 3]))
print(computadora)

if jugador == 1 and computadora == 1:
    print("Empate")
elif jugador == 1 and computadora == 2:
    print("Gano computadora")
elif jugador == 1 and computadora == 3:
    print("Gano jugador")
elif jugador == 2 and computadora == 1:
    print("Gano jugador")
elif jugador == 2 and computadora == 2:
    print("Empate")
elif jugador == 2 and computadora == 3:
    print("Gano computadora")
elif jugador == 3 and computadora == 1:
    print("Gano computadora")
elif jugador == 3 and computadora == 2:
    print("Gano jugador")
elif jugador == 3 and computadora == 3:
    print("Empate")
else:
    print("Opcion no valida....")



print("Fin del juego")
