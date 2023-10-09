# Calculadora de factorial:
# Desarrolla un programa que calcule el factorial de un número ingresado por el usuario

print("Inicio de programa")

indicador = int(input("Ingrese el numero del factorial deseado :"))
resultado = 1
acum = 1

for i in range(indicador):
    print("x")
    resultado = resultado * acum
    acum = acum+1


print("El resultado es : ", resultado)

print("Fin del programa")
