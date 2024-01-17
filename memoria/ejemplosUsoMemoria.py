# #convenciones nombres variables

# nombre_paterno = "" #snake case

# NOMBRE_PATERNO = "" #screaming snake case

# NombrePaterno = "" #upper camell case

# nombrePaterno = "" #lower camell case


# #ejemplo memoria estatica

# edad = 25
# nombre = "Irving"
# lista_estatica = [1,3,5,7,9]

# #ejemplo memoria dinamica

# lista_dinamica = [2,4,6,8]

# print("Hola", nombre)
# print("Selecciona un numero: ")

# print(lista_estatica)
# add_lista = int(input("ingrese numero: "))
# lista_dinamica.append(add_lista)
# print(lista_dinamica)


#uso de momeria dinamica en objetos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Irving", 25)

print(persona1)
