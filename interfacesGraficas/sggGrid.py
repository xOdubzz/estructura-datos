import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con grid")

label = tk.Label(root, text= "Hola tkinter")
label.grid(row = 0, column= 0, sticky="nsew")

boton = tk.Button(root, text="Click aqui")
boton.grid(row=1, column=2, sticky="nsew")

entrada = tk.Entry(root)
entrada.grid(row=2, column=3, sticky="nsew")

root.mainloop()