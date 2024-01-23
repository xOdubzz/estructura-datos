#hacer un programa que cature los siguientes datos de alumnos
#nombre, apellido paterno, apellido materno, fecha de nacimiento eb fornato dia/mes/ano
#guardar los datos en objetos
#mostrar esos objetos

class Alumno:
    alumnos = []

    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        Alumno.alumnos.append(self)

    def mostrar_alumnos(self):
        print("Lista de alumnos:")
        for alumno in Alumno.alumnos:
            print(f"Nombre: {alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno}")
            print(f"Fecha de Nacimiento: {alumno.fecha_nacimiento}")
            print("------")



num_alumnos = int(input("Ingrese el número de alumnos: "))

for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    apellido_paterno = input(f"Ingrese el apellido paterno del alumno {i + 1}: ")
    apellido_materno = input(f"Ingrese el apellido materno del alumno {i + 1}: ")
    fecha_nacimiento = input(f"Ingrese la fecha de nacimiento (dd/mm/aaaa) del alumno {i + 1}: ")

    # Crear objeto Alumno y almacenar en la lista
    alumno = Alumno(nombre, apellido_paterno, apellido_materno, fecha_nacimiento)


Alumno.mostrar_alumnos()


