#Declaramos dos vectores 
#Estos vectores seran homogeneos

nombres = []
identificadores = []

suma = []

#Definimos un tamano para las listas o vectores
#Lo puedes cambiar si queires, antes de la compilacion
size = 3

for i in range(size):
    print("Ingrese los datos de la persona", i + 1)
    input_nombre = input("Nombre: ")
    identificacion = input("Identificacion: ")
    
    nombres.append(input_nombre)
    identificadores.append(identificacion)


print(nombres)
print(identificadores)

suma.append(nombres)
suma.append(identificadores)
print("Sumando Vectores")
print(suma) # El resultado es un vector heterogeneo

