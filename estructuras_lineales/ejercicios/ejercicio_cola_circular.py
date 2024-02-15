from collections import deque

def rotacion_empleados(empleados, turnos):
    cola_empleados = deque(empleados)

    for _ in range(turnos):
        empleado_actual = cola_empleados.popleft()
        cola_empleados.append(empleado_actual)
        print("Empleado en turno:", cola_empleados[0])

empleados = ["francisco", 'rafa', 'Irving', 'pedro']

rotacion_empleados(empleados, 7)