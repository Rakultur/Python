# 6 Conversor de unidades:
# Haz un programa que convierta entre diferentes unidades, como de grados Celsius a Fahrenheit o de kilómetros a millas,
# según la elección del usuario.

print("Inicio del programa")

indicador = True

while indicador == True:
    print(
        "Seleccion operacion a realizar : \n 1. Grador C a F \n 2. Km a Millas \n 3.Salir"
    )
    selector = int(input(""))
    # Selector de grados
    if selector == 1:
        print("Conversor Grados")
        selector_2 = int(input("1. Celsius a Fahrenheit \n 2. Fahrenheit a Celsius"))
        if selector_2 == 1:
            celsius = float(input("Ingrese los grados celsius : "))
            r_1 = (celsius * 1.8) + 32
            print("Los gados Fahrenheit son : ", r_1)
            celsius = 0
        elif selector_2 == 2:
            fahrenheit = float(input("Ingrese los grados Fahrenheit : "))
            r_2 = (fahrenheit - 32) / 1.8
            print("Los gados Celsius son : ", r_2)
            fahrenheit = 0
        else:
            print("Respuesta incorrecta")
    # Selector de velocidad
    elif selector == 2:
        print("Conversor Velocidades")
        selector_3 = int(input("1. km a millas \n 2. millas a km"))
        if selector_3 == 1:
            kilometros = float(input("Ingrese el valor de kilometros : "))
            r_3 = kilometros / 1.609344
            print("Las millas son : ", r_3)
            kilometros = 0
        elif selector_3 == 2:
            millas = float(input("Ingrse el valor de las millas : "))
            r_4 = millas * 1.609344
            print("Los kilometros son : ", r_4)
            millas = 0
        else:
            print("Respuesta incorrecta")
    # Salida
    elif selector == 3:
        indicador = False
    else:
        print("La respues no es correcta vuelva a intentar...")

print("Fin del programa")
