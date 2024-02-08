#hacer una interfaz grafica que calcule el curp simple
#capturar nombre, apellido patern, apellido materno y fecha de nacimiento
#cuando se genere, mostrar un mensaje de que se ha generado la curp

import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de CURP simple")

        self.frame = tk.Frame(root, width=600, height=500, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        self.etiquerta1 = tk.Label(self.frame, text="Nombre Completo:")
        self.etiquerta1.place(x= 20, y= 30)

        self.etiqueta2 = tk.Label(self.frame, text="Fecha de Nacimiento:")
        self.etiqueta2.place(x= 20, y=60)

        self.entrada1 = tk.Entry(root, width= 30)
        self.entrada1.place(x= 180, y= 60)

        self.entrada2 = tk.Entry(root, width= 15)
        self.entrada2.place(x= 200, y=90)

        self.boton = tk.Button(self.frame, text= "Generar CURP", command= generador_curp)
        self.boton.place(x= 150, y= 120)

        self.etiquerta1_curp = tk.StringVar()

    def generador_curp(self):
        
        nombre = input("Ingrese nombre completo iniciando por apellidos: ")
        nombree = nombre.upper()
        vnombre = nombree.split(' ')

        size = len(vnombre)

        curp = []

        for i in range(size):
            separado = vnombre[i]
            inicial = separado[0]
            curp.append(inicial)

        curp = self.etiquerta1_curp
        self.etiquerta1_curp.set()


    



root = tk.Tk()

app = App(root)

root.minsize(600, 500)

root.mainloop()