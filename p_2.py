# Contador de números pares e impares:
# Escribe un programa que cuente cuántos números pares e impares hay en una lista de números ingresada por el usuario.
print("Inicio de programa")

indicador = int(input("Ingrese la cantidad de numeros a digitar :"))

impares=0

pares=0

for i in range(indicador):
   numero = float(input("ingrese el valor : "   ))
   if (numero%2) == 0:
     pares = pares+1
     numero == 0 
   else:
     impares = impares+1
     numero == 0 

   
print("El total de pares  es : " , pares)
print("El total de impares es : " , impares)

print("Fin de programa")