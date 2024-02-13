#Definicion:
#Es una estructura de datos, en la que los mismos se van almacenando a manera de pila, es decir
#uno por encima de otro
#Usa el principio LIFO

pila = [] #definimos nuestra pila vacia

#push - operacion para agregar elementos

pila.append(18)
pila.append(25)
pila.append(56)

print(pila)

peek = pila.pop()

print("El elemento sacado de la pila fue", peek)

pilaString = []

pilaString.append("Rafa")
pilaString.append("Irving")
pilaString.append("Pedro")
pilaString.append("Francisco")
print(pilaString)
pilaString.pop()
print(pilaString)
cima = pilaString.pop()
print("La cima es", cima)
print(pilaString)