import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Uso de Frame")

        # Crear un frame con tamaño específico
        self.frame = tk.Frame(root, width=200, height=150, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        # Widgets dentro del frame
        self.label1 = tk.Label(self.frame, text="Etiqueta 1")
        self.label1.grid(row=0, column=0)

        self.label2 = tk.Label(self.frame, text="Etiqueta 2")
        self.label2.grid(row=0, column=1)

        self.boton = tk.Button(self.frame, text="Botón", command=self.hacer_algo)
        self.boton.grid(row=1, columnspan=2)

        self.boton2 = tk.Button(self.frame, text="Boton 2", command=self.error)
        self.boton2.grid(row=2, column=3)

        self.boton3 = tk.Button(self.frame, text = "Boton advertencia", command=self.advertencia)
        self.boton3.grid(row=3, column= 3)

        self.entrada_num1 = tk.Entry(root)
        self.entrada_num1.place(x= 100, y=30)

        self.entrada_num2 = tk.Entry(root)
        self.entrada_num2.place(x= 100, y=60)

        self.resultado = tk.StringVar()

        self.etiqueta_num1 = tk.Label(root, text="numero 1")
        self.etiqueta_num1.place(x=30, y=30)

        self.etiqueta_num2 = tk.Label(root, text="numero 2")
        self.etiqueta_num2.place(x=30, y=60)

        self.etiqueta_resultado = tk.Label(root, textvariable=self.resultado)
        self.etiqueta_resultado.place(x=140, y=100)


        self.boton_sumar = tk.Button(root, text="Sumar", command=self.sumar_numeros)
        self.boton_sumar.place(x=150, y=150)



    def hacer_algo(self):
        print("Haciendo algo...")
        messagebox.showinfo("Mensaje", "que hongo")

    def advertencia(self):
        print("Advertencia")
        messagebox.showwarning("Advertencia", "Estas advertido")

    def error(self):
        print("Error")
        messagebox.showerror("Error", "Ha ocurrido un error")

    def sumar_numeros(self):
        try:

            num1 = float(self.entrada_num1.get())
            num2 = float(self.entrada_num2.get())

            self.resultado.set(f"Resultado {num1 + num2}")



        except ValueError:
            self.resultado.set(f"ERROR: Ingrese numeros validos")
# Crear ventana principal
root = tk.Tk()

# Iniciar la aplicación y pasar la ventana principal
app = App(root)

# Establecer tamaño mínimo de la ventana principal
root.minsize(400,300)

# Ejecutar el bucle principal
root.mainloop()


import time
import tkinter as tk





def cronometro(tiempo_total):
    tiempo_inicial = time.time()

    while True:
        tiempo_transcurrido = time.time() - tiempo_inicial

        minutos, segundos = divmod(tiempo_transcurrido, 60)
        minutos = int(minutos)
        segundos = int(segundos)

        print(f"{minutos:02d}:{segundos:02d}", end="\r")

        if tiempo_transcurrido >= tiempo_total:
            break

        time.sleep(1)

    print("\n¡Tiempo finalizado!")

# Configura el tiempo total en segundos para el cronómetro
tiempo_total = 300  # Ejemplo: 5 minutos

cronometro(tiempo_total)