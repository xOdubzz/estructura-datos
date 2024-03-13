import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class NodoArticulo():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.siguiente = None


class ListaEnlazada():
    def __init__(self):
        self.cabeza = None

    def agregar_al_principio(self, nombre, precio):
        nuevo_nodo = NodoArticulo(nombre, precio)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, nombre):
        actual = self.cabeza
        previo = None
        while actual and actual.nombre != nombre:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.nombre, actual.precio)
            actual = actual.siguiente

    def obtener_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append((actual.nombre, actual.precio))
            actual = actual.siguiente
        return lista


class ColaPedidos():
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None


class PilaVentas():
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


class RestauranteApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación de Restaurante")
        self.tabControl = ttk.Notebook(self)

        self.tabArticulos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabArticulos, text="Artículos")

        self.tabPedidos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabPedidos, text="Pedidos")

        self.tabVentas = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabVentas, text="Ventas")

        self.tabControl.pack(expand=1, fill="both")

        self.lista_articulos = ListaEnlazada()
        self.cola_pedidos = ColaPedidos()
        self.pila_ventas = PilaVentas()

        self.create_articulos_widgets()
        self.create_pedidos_widgets()
        self.create_ventas_widgets()

    def create_articulos_widgets(self):
        frame_articulos = ttk.LabelFrame(self.tabArticulos, text="Gestión de Artículos")
        frame_articulos.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_nombre = tk.Label(frame_articulos, text="Nombre:")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_articulos)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        lbl_precio = tk.Label(frame_articulos, text="Precio:")
        lbl_precio.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_precio = tk.Entry(frame_articulos)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        btn_agregar = tk.Button(frame_articulos, text="Agregar Artículo", command=self.agregar_articulo)
        btn_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        btn_eliminar = tk.Button(frame_articulos, text="Eliminar Artículo", command=self.eliminar_articulo)
        btn_eliminar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_articulos = tk.Listbox(frame_articulos)
        self.listbox_articulos.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def agregar_articulo(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        if nombre and precio:
            self.lista_articulos.agregar_al_principio(nombre, precio)
            self.actualizar_lista_articulos()
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            messagebox.showinfo("Información", "Artículo agregado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el nombre y precio del artículo.")

    def eliminar_articulo(self):
        seleccionado = self.listbox_articulos.curselection()
        if seleccionado:
            indice = seleccionado[0]
            nombre = self.listbox_articulos.get(indice).split()[0]  # Obtener el nombre del artículo
            self.lista_articulos.eliminar(nombre)
            self.actualizar_lista_articulos()
            messagebox.showinfo("Información", "Artículo eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor selecciona un artículo.")

    def actualizar_lista_articulos(self):
        self.listbox_articulos.delete(0, tk.END)
        articulos = self.lista_articulos.obtener_lista()
        for articulo in articulos:
            self.listbox_articulos.insert(tk.END, f"{articulo[0]} - ${articulo[1]}")

    def create_pedidos_widgets(self):
        frame_pedidos = ttk.LabelFrame(self.tabPedidos, text="Gestión de Pedidos")
        frame_pedidos.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_pedido = tk.Label(frame_pedidos, text="Pedido:")
        lbl_pedido.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_pedido = tk.Entry(frame_pedidos)
        self.entry_pedido.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_hacer_pedido = tk.Button(frame_pedidos, text="Hacer Pedido", command=self.hacer_pedido)
        btn_hacer_pedido.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        btn_pedido_realizado = tk.Button(frame_pedidos, text="Pedido Realizado", command=self.pedido_realizado)
        btn_pedido_realizado.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_pedidos = tk.Listbox(frame_pedidos)
        self.listbox_pedidos.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def hacer_pedido(self):
        pedido = self.entry_pedido.get()
        if pedido:
            self.cola_pedidos.encolar(pedido)
            self.actualizar_lista_pedidos()
            self.entry_pedido.delete(0, tk.END)
            messagebox.showinfo("Información", "Pedido realizado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el pedido.")

    def pedido_realizado(self):
        pedido = self.cola_pedidos.desencolar()
        if pedido:
            self.pila_ventas.apilar(pedido)
            messagebox.showinfo("Información", f"Pedido realizado: {pedido}")
            self.actualizar_lista_pedidos()
        else:
            messagebox.showinfo("Información", "No hay pedidos pendientes.")

    def actualizar_lista_pedidos(self):
        self.listbox_pedidos.delete(0, tk.END)
        pedidos = self.cola_pedidos.items
        for pedido in pedidos:
            self.listbox_pedidos.insert(tk.END, pedido)

    def create_ventas_widgets(self):
        frame_ventas = ttk.LabelFrame(self.tabVentas, text="Gestión de Ventas")
        frame_ventas.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_venta = tk.Label(frame_ventas, text="Venta:")
        lbl_venta.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_venta = tk.Entry(frame_ventas)
        self.entry_venta.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_realizar_venta = tk.Button(frame_ventas, text="Realizar Venta", command=self.realizar_venta)
        btn_realizar_venta.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        btn_devolucion = tk.Button(frame_ventas, text="Devolución", command=self.devolucion)
        btn_devolucion.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_ventas = tk.Listbox(frame_ventas)
        self.listbox_ventas.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def realizar_venta(self):
        venta = self.entry_venta.get()
        if venta:
            self.pila_ventas.apilar(venta)
            self.actualizar_lista_ventas()
            self.entry_venta.delete(0, tk.END)
            messagebox.showinfo("Información", "Venta realizada correctamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa la venta.")

    def devolucion(self):
        venta = self.pila_ventas.desapilar()
        if venta:
            messagebox.showinfo("Información", f"Devolución realizada: {venta}")
            self.actualizar_lista_ventas()
        else:
            messagebox.showinfo("Información", "No hay ventas realizadas para devolver.")

    def actualizar_lista_ventas(self):
        self.listbox_ventas.delete(0, tk.END)
        ventas = self.pila_ventas.items
        for venta in ventas:
            self.listbox_ventas.insert(tk.END, venta)


if __name__ == "__main__":
    app = RestauranteApp()
    app.mainloop()