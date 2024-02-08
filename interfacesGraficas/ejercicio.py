import tkinter as tk



def sumar_numeros():
    try:

        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        resultado.set(f"Resultado {num1 + num2}")



    except ValueError:
        resultado.set(f"ERROR: Ingrese numeros validos")


#crear ventana principal
        
root = tk.Tk()
root.title("Calculadora simple")

entrada_num1 = tk.Entry(root)
entrada_num1.place(x= 100, y=30)
entrada_num2 = tk.Entry(root)
entrada_num2.place(x= 100, y=60)
resultado = tk.StringVar()

etiqueta_num1 = tk.Label(root, text="numero 1")
etiqueta_num1.place(x=30, y=30)
etiqueta_num2 = tk.Label(root, text="numero 2")
etiqueta_num2.place(x=30, y=60)
etiqueta_resultado = tk.Label(root, textvariable=resultado)
etiqueta_resultado.place(x=140, y=100)

#usar sgg preferida


#

boton_sumar = tk.Button(root, text="Sumar", command=sumar_numeros)
boton_sumar.place(x=150, y=150)

root.mainloop()