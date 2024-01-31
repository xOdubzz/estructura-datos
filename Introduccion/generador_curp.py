#hacer un programa que genera una CURP hipotetica tomando lig. criterios
#inicial del apellido paterno Paterno y materno,
nombre = input("Ingrese nombre completo iniciando por apellidos: ")
nombree = nombre.upper()
vnombre = nombree.split(' ')

size = len(vnombre)

curp = []

for i in range(size):
    separado = vnombre[i]
    inicial = separado[0]
    curp.append(inicial)

print("Tu curp es: ", *curp)
