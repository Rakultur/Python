# Tabla de multiplicar:
# Pide al usuario un número y muestra la tabla de multiplicar correspondiente a ese número, desde 1 hasta 10.

print("Inicio de programa")
indicador = float(input("Ingrese el numero a multiplicar hasta 10 : "))

for i in range(11):
    print(indicador,"x",i,":",indicador*i)
 

print("Fin del programa")