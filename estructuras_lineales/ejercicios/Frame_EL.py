import tkinter as tk
from tkinter import messagebox

class FrameEl(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)

        self.master = master
        self.ordenes = []

        self.texto_label = tk.Label(self, text="Orden Actual: ")
        self.texto_label.pack()

        self.texto_var = tk.StringVar()
        self.texto_actual = tk.Label(self, textvariable = self.texto_var)
        self.texto_actual.pack()

        self.boton_opcion1 = tk.Button(self, text="Opcion 1", command=self.agregar_opcion1)
        self.boton_opcion1.pack()

        self.boton_opcion1 = tk.Button(self, text="Opcion 2", command=self.agregar_opcion2)
        self.boton_opcion1.pack()
        
    def agregar_opcion1(self):

        texto_nuevo = "Opcion 1"
        self.ordenes.append(texto_nuevo)
        self.actualizar_orden()

    def agregar_opcion2(self):

        texto_nuevo = "Opcion 2"
        self.ordenes.append(texto_nuevo)
        self.actualizar_orden()

    
    def actualizar_orden(self):
        
        texto_actual = ''.join(self.ordenes)
        self.texto_var.set(texto_actual)


root = tk.Tk()
editor_frame = FrameEl(master=root)
editor_frame.pack()
editor_frame.mainloop()