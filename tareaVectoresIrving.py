# Crear un programa que almacene nombres en un vector
#capturara datos hasta que el valor ingresado sea "STOP"
#mostrar el vector resultante
# sugerencia: usar while

nombres = []

while True:
    nombre = str(input("Ingresa un nombre: "))
    if nombre == "STOP":
        False
    else:
        nombres.append(nombre)

print("Nombres almacenados: ", nombres)