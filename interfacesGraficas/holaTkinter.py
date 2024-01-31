import tkinter as tk

def boton_clic():
    print("Boton clickeado")

#def boton_texto():


root = tk.Tk()
root.title("Mi aplicacion Tkinter")

# label = tk.Label(root, text = "Hola, Tkinter!")

# #configurar el sistema de gestion de geometria

# label.pack()

boton = tk.Button(root, text="Clic aqui", command=boton_clic)
boton.pack()


# boton = tk.Button(root, text="Mostrar texto", command=boton_texto)
# boton.pack()

entrada = tk.Entry(root)
entrada.pack()

root.mainloop()