class Tareas:

    tareas = []

    def __init__(self, nombre, fecha_in, fecha_fin):
        self.nombre = nombre
        self.fecha_in = fecha_in
        self.fecha_fin = fecha_fin
        Tareas.tareas.append(self)

    def mostrar_tareas():
        for i in Tareas.tareas:
            print(f"Las tareas pendientes son: {i.nombre}, fecha inicial: {i.fecha_in}, fecha limite: {i.fecha_fin}")

n_tareas = int(input("Ingrese el numero de tareas que se agregaran: "))

for i in range(n_tareas):
    nombre = input("nombre de la tarea: ")
    fecha_in = input("ingresa la fecha incial de la tarea en formato dd/mm/aaaa: ")
    fecha_fin = input("ingresa la fecha limite de entrega de la tarea en formato dd/mm/aaaa: ")

    tarea = Tareas(nombre, fecha_in, fecha_fin)

Tareas.mostrar_tareas()