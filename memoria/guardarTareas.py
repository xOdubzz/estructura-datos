class Tareas:

    tareas = []

    def __init__(self, nombre, fecha_in, fecha_fin):
        self.nombre = nombre
        self.fecha_in = fecha_in
        self.fecha_fin = fecha_fin
        Tareas.tareas.append(self)

    def pedir_tareas(cls):
        nombre = input("Ingrese el nombre de la tarea a realizar: ")
        fecha_in = input("Ingresa la ficha incial en formato dd/mm/aaaa: ")
        fecha_fin = input("Ingresa la fecha limite de entrega en formato dd/mm/aaaa: ")

        n_tarea = cls(nombre, fecha_in, fecha_fin)

    def mostrar_tareas(cls):
        for i in Tareas.tareas:
            print(f"Las tareas pendientes son: {i.nombre}, fecha inicial: {i.fecha_in}, fecha limite: {i.fecha_fin}")


a_tareas = Tareas()

a_tareas.pedir_tareas()

a_tareas.mostrar_tareas()