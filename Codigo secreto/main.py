# Importar libreriras
import pyttsx3
import msvcrt
from variables import * 
from logica import *

# Se crea un objeto para la reproducir de voz
voz = pyttsx3.init()
# Saludo y bienvenida al programa
print("¡Bienvenido!")
voz.say("Bienvenido usuario al programa para cifrar y decifrar mensajes...")
voz.runAndWait()
# Inicio del ciclo  
while indicador == 1:
    voz.say("Por favor, seleccione una de las opciones : ....")
    voz.runAndWait()
    print("1. Cifrar ")
    print("2. Decifrar ")
    indicador_2 = input("   ")
    try:
        indicador_2 = float(indicador_2)
        # Cifrado
        if indicador_2 == 1:
            voz.say("Su respuesta es Cifrar, por favor ingrese el texto....")
            voz.runAndWait()
            cifrar()
            lista_2.pop
            print("Fin del programa")
            indicador = indicador+1
        # Decifrado
        elif indicador_2 == 2:
            voz.say("Su respuesta es Decifrar, por favor ingrese el texto....")
            voz.runAndWait()
            decifrar()
            lista_3.pop
            print("Fin del programa")
            indicador = indicador+1
    except:
        voz.say("Algo ha salido mal, por favor intentelo nuevamente .......")
        voz.runAndWait
        
msvcrt.getch()