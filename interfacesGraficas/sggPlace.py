import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con place()")

label = tk.Label(root, text="hola tkinter!")
label.place(x=10, y=10)

boton = tk.Button(root, text="click aqui")
boton.place(x=10, y=28)

entrada = tk.Entry(root)
entrada.place(x=10, y=70)

root.mainloop()