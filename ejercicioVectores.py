#Crear un programa que pida "x" cantidad de numeros
#y separar los numeros pares en un vector y los nones en otro, y al final mostrar ambos vectoes

pares = []
nones = []
suma = []
size = 4

for i in range(size):
    print("Ingresa un numero ", i + 1)
    numero = int(input("Numero: "))
    clasificador = numero % 2
    if clasificador == 0:
        pares.append(numero)
    else:
        nones.append(numero)

suma.append(pares)
suma.append(nones)
print("Numeros pares: ", pares)
print("Numeros impares: ", nones)
print("Valores recolectados: ", suma)
