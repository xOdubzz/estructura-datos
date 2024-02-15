from collections import deque

#implementacion de un sistema de gestion de tareas pendientes

class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = deque()

    def agregar_tareas(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(self.tareas_pendientes)
    def procesar_tareas(self):
        while self.tareas_pendientes:
            tarea = self.tareas_pendientes.popleft()
            print("Procesando tarea:", tarea)

#ejemplo de uso
            
sistema = SistemaGestionTareas()
sistema.agregar_tareas("Banarse")
sistema.agregar_tareas("tender camaa")
sistema.agregar_tareas("Desayunar")
sistema.procesar_tareas()