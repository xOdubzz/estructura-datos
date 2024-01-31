import tkinter as tk



def sumar_numeros(a, b):
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
entrada_num2 = tk.Entry(root)
resultado = tk.StringVar()

etiqueta_num1 = tk.Label(root, text="numero 1")
etiqueta_num2 = tk.Label(root, text="numero 2")
resultado = tk.Label(root, textvariable=resultado)

#usar sgg preferida


#

boton_sumar = tk.Button(root, text="Sumar", command=sumar_numeros)

root.mainloop()
