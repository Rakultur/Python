# 8Lista de la compra:
# Diseña un programa que permita al usuario crear una lista de compras
# agregar elementos, eliminar elementos y mostrar la lista final.


print("Inicio del programa")

selector = True
consecutivo = 0
lista = []

while selector == True:
    print("1. Agregar item \n 2. Eliminar item \n 3. Mostrar lista \n 4. Salir")
    indicador = int(input(""))
    if indicador == 1:
        print("Agregar : ")
        lista.append(input(""))
        consecutivo = consecutivo + 1
    elif indicador == 2:
        print("Eliminar : ")
        print(lista)
        r = input("Seleccione item a eliminar")
        try:
            lista.remove(r)
            print("Item eliminado...")
        except:
            print("Item incorrecto...")
    elif indicador == 3:
        print("Tu lista : ")
        print(lista)
    elif indicador == 4:
        print("Adios.")
        selector = False
    else:
        print("Indicador incorrecto, vuelve a intentar...")

print("Fin del programa")
