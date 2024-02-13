#Definicion
#Un estructura que va almacenando datos uno detras de otro, tal como su nombre lo indica
#en el que, como en una cola, el primero en entrar es el primero en salir
#Usa principio FIFO

from collections import deque

cola = deque()

#encolar

cola.append("Rafa")
cola.append("Irving")
cola.append("Pedro")
cola.append("Willmar")

print(cola)

cola.appendleft("Francisco")

print(cola)
#print(cola[0])

#desencolar

elemento = cola.popleft()
print(elemento)
