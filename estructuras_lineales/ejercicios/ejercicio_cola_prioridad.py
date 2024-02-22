import heapq

class SistemaPlanificacionTareas:
    def __init__(self):
        #inicializamos la cola
        self.tareas = []

    def agregar_tareas(self, tarea, prioridad):
        #encolar
        heapq.heappush(self.tareas, (prioridad, tarea))

    def procesar_tareas(self):
        #mostrar tareas encoladas
        while self.tareas:
            prioridad, tarea = heapq.heappop(self.tareas)
            print("Procesando tarea: ", tarea, "(prioridad: ", prioridad )

sistema = SistemaPlanificacionTareas()
sistema.agregar_tareas("Comer", 4)
sistema.agregar_tareas("despertar", 3)
sistema.agregar_tareas("sas", 2)
sistema.agregar_tareas("slals", 1)

sistema.procesar_tareas()
