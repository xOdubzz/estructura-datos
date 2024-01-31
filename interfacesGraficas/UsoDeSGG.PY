#grid y pack no se juntan


import tkinter as tk

root = tk.Tk()
root.title("Ejemplo combinando metodos")

#pack
# label = tk.Label(root, text="Hola tkinter")
# label.pack(side="top", fill="x")

#grid
boton = tk.Button(root, text="Click aqui")
boton.grid(row=1, column= 0, sticky="nsew")

boton = tk.Button(root, text="Click aqui")
boton.grid(row=1, column= 1, sticky="nsew")

#place
entrada = tk.Entry(root)
entrada.place(x=10, y=70)

root.mainloop()