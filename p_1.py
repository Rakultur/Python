# Calculadora simple:
# Crea un programa que solicite dos números al usuario y realice operaciones básicas como suma, resta, multiplicación y división con esos números

print("Inicio de programa")

n1 = float(input("Ingrese primer numero :"))
n2 = float(input("Ingrese segundo numero :"))

# Suma

suma = n1 + n2
print("El resultado de la operacion suma es :" , suma)

# Resta

resta = n1 - n2
print("El resultado de la operacion resta es :" , resta)

# multiplicación

multiplicación = n1 * n2
print("El resultado de la operacion multiplicación es :" , multiplicación)

# división

if n2 == 0:
    print("No se puede divir por 0")
elif n2 != 0:
    división = n1 / n2
    print("El resultado de la operacion división es :" , división)

print("Fin del programa")
