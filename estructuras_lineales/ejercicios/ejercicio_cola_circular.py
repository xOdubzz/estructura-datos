#ejercicio cola circular
from collections import deque

#implementacion de un simulador de rotacion de empleados en turnos
def rotacion_empleados(empleados, turnos):
    cola_empleados = deque(empleados)

    for _ in range(turnos):
        empleado_actual = cola_empleados.popleft()
        cola_empleados.append(empleado_actual)
        print("Empleado en turno:", cola_empleados[0])


#ejemplo de uso
empleados = ["francisco", 'rafa', 'Irving', 'pedro']

rotacion_empleados(empleados, 7)