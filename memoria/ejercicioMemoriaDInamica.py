#hacer un programa que cature los siguientes datos de alumnos
#nombre, apellido paterno, apellido materno, fecha de nacimiento eb fornato dia/mes/ano
#guardar los datos en objetos
#mostrar esos objetos

class Alumnos:
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_alumnos(self):
        print("Datos del alumno: ", self.nombre, self.apellido_paterno, self.apellido_materno, self.fecha_nacimiento)


vAlumos = []

while True:

    print("Ingrese los datos, escriba STOP para terminar")

    alumno = input("Nombre del alumnos: ")
    vAlumos.append(alumno)
    


