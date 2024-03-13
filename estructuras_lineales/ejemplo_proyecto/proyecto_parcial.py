import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class NodoListaEnlazada():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class NodoListaEnlazadaPrecios():
    def __init__(self, dato_p):
        self.dato_p = dato_p
        self.siguiente_p = None

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None

    def agregar_al_principio(self, dato):
        nuevo_nodo = NodoListaEnlazada(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual and actual.dato != dato:
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
            print(actual.dato)
            actual = actual.siguiente

    def obtener_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        return lista

class ListaEnlazadaPrecio():
    def __init__(self):
        self.cabeza_p = None

    def agregar_al_principio(self, dato):
        nuevo_nodo_p = NodoListaEnlazadaPrecios(dato)
        nuevo_nodo_p.siguiente_p = self.cabeza_p
        self.cabeza_p = nuevo_nodo_p

    def eliminar(self, dato):
        actual_p = self.cabeza_p
        previo_p = None
        while actual_p and actual_p.dato_p != dato:
            previo_p = actual_p
            actual_p = actual_p.siguiente_p
        if actual_p:
            if previo_p:
                previo_p.siguiente_p = actual_p.siguiente_p
            else:
                self.cabeza_p = actual_p.siguiente_p

    def mostrar_lista(self):
        actual_p = self.cabeza_p
        while actual_p:
            print(actual_p.dato_p)
            actual_p = actual_p.siguiente_p

    def obtener_lista(self):
        lista_p = []
        actual_p = self.cabeza_p
        while actual_p:
            lista_p.append(actual_p.dato_p)
            actual_p = actual_p.siguiente_p
        return lista_p

class ColaCircular():
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_primero(self):
        return self.items[-1]

    def avanzar_turno(self):
        if not self.esta_vacia():
            self.items.append(self.items.pop(0))

class HistorialOrdenes:
    def __init__(self):
        self.pila_ordenes = []

    def agregar_orden(self, orden):
        self.pila_ordenes.append(orden)

    def deshacer_ultima_orden(self):
        if self.pila_ordenes:
            return self.pila_ordenes.pop()
        else:
            return None
class PilaVentas():
    def _init_(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None


class RestauranteApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tiendita -La Reniza- ")
        self.tabControl = ttk.Notebook(self)

        self.tabProductos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabProductos, text="Productos")

        self.tabPedidos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabPedidos, text="Pedidos")

        self.tabVentas = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabVentas, text="Ventas")

        #self.tabHistorial = ttk.Frame(self.tabControl)
        #self.tabControl.add(self.tabHistorial, text="Historial")

        #self.tabReservas = ttk.Frame(self.tabControl)
        #self.tabControl.add(self.tabReservas, text="Reservas")

        # Acomodar Pestañas
        self.tabControl.pack(expand=1, fill="both")

        # Definir la lista enlazada de empleados
        self.lista_productos = ListaEnlazada()
        self.lista_precios = ListaEnlazadaPrecio()

        #Definir la cola circular de turnos
        self.cola_pedidos = ColaCircular()

        # Definir la pila para el historial de órdenes
        #self.historial_ordenes = HistorialOrdenes()
        self.pila_ventas = PilaVentas()


        # Llamar métodos para definir Pestañas
    #     self.create_empleados_widgets()
    #     self.create_turnos_widgets()
    #     self.create_ordenes_widgets()
    #     self.create_historial_widgets()
    #     self.create_reservas_widgets()
        self.create_empleados_widgets()
        self.create_pedidos_widgets()
        self.create_ventas_widgets()


    def create_empleados_widgets(self):
    #     # Pestaña Empleados
        frame_productos = ttk.LabelFrame(self.tabProductos, text="Listado de Productos")
        frame_productos.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_nombre = tk.Label(frame_productos, text="Producto:")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        self.entry_producto = tk.Entry(frame_productos)
        self.entry_producto.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        lbl_precio = tk.Label(frame_productos, text="Precio:")
        lbl_precio.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.entry_precio = tk.Entry(frame_productos)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        btn_agregar = tk.Button(frame_productos, text="Agregar Producto", command= self.a_p)
        btn_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_productos = tk.Listbox(frame_productos)
        self.listbox_productos.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.listbox_precios = tk.Listbox(frame_productos)
        self.listbox_precios.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

    def a_p(self):
        self.agregar_producto()
        self.agregar_precio()
    
    def agregar_producto(self):
        nombre_producto = self.entry_producto.get()
        if nombre_producto:
            self.lista_productos.agregar_al_principio(nombre_producto.upper())
            self.actualizar_lista_productos()
            self.entry_producto.delete(0, tk.END)
            messagebox.showinfo("Información", "Producto agregado exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el producto.")

    def actualizar_lista_productos(self):
        self.listbox_productos.delete(0, tk.END)
        productos = self.lista_productos.obtener_lista()
        for producto in productos:
            self.listbox_productos.insert(tk.END, producto)
    
    def agregar_precio(self):
        precio_producto = self.entry_precio.get()
        if precio_producto:
            self.lista_precios.agregar_al_principio(precio_producto)
            self.actualizar_lista_precios()
            self.entry_precio.delete(0, tk.END)
            messagebox.showinfo("Información", "Producto agregado exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el producto.")

    def actualizar_lista_precios(self):
        self.listbox_precios.delete(0, tk.END)
        precios = self.lista_precios.obtener_lista()
        for precio in precios:
            self.listbox_precios.insert(tk.END, precio + " MXN")

    def create_pedidos_widgets(self):
    #     # Pestaña Turnos
        frame_pedidos = ttk.Frame(self.tabPedidos)
        frame_pedidos.pack(fill="both", expand=True)

        lbl_pedido = tk.Label(frame_pedidos, text="Turno:")
        lbl_pedido.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_pedido = tk.Entry(frame_pedidos)
        self.entry_pedido.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_realizar_pedido = tk.Button(frame_pedidos, 
                                      text="Realizar Pedido", 
                                      command=self.realizar_pedido)
        btn_realizar_pedido.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        btn_avanzar_pedido = tk.Button(frame_pedidos, text="Terminar Pedido",
                                       command=self.terminar_pedido)
        btn_avanzar_pedido.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_pedidos = tk.Listbox(frame_pedidos)
        self.listbox_pedidos.grid(row=3, column=0, columnspan=2, 
                                 padx=5, pady=5, sticky="nsew")

    def realizar_pedido(self):
        pedido = self.entry_pedido.get()
        if pedido:
            #producto = self.lista_productos.obtener_lista().pop(0)
            self.cola_pedidos.encolar((pedido))
            self.actualizar_lista_pedidos()
            self.entry_pedido.delete(0, tk.END)
            messagebox.showinfo("Información", 
                                f"Pedido realizado.")
        else:
            messagebox.showerror("Error", "Por favor haga un pedido.")

    def terminar_pedido(self):
        pedido = self.cola_pedidos.desencolar()
        if pedido:
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
        frame_ventas = ttk.LabelFrame(self.tabVentas, text="Realizar Venta")
        frame_ventas.pack(padx=10, pady=10, fill="both", expand=True)

        productos_precios = [("Sopa", 20), ("Refresco", 25), ("Papas", 30), ("Galletas", 15)]
        self.listbox_productos_precios = tk.Listbox(frame_ventas, selectmode=tk.SINGLE)
        for producto, precio in productos_precios:
            self.listbox_productos_precios.insert(tk.END, f"{producto} - {precio} MXN")
        self.listbox_productos_precios.grid(row=0, column=0, padx=5, pady=5, rowspan=4)

        lbl_cantidad = tk.Label(frame_ventas, text="Cantidad:")
        lbl_cantidad.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.entry_cantidad_venta = tk.Entry(frame_ventas)
        self.entry_cantidad_venta.grid(row=0, column=2, padx=5, pady=5)

        btn_realizar_venta = tk.Button(frame_ventas, text="Realizar Venta", command=self.realizar_venta)
        btn_realizar_venta.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    def realizar_venta(self):
        seleccion = self.listbox_productos_precios.curselection()
        if seleccion:
            indice_seleccionado = seleccion[0]
            producto_precio = self.listbox_productos_precios.get(indice_seleccionado)
            _, precio_str = producto_precio.split(" - ")
            precio = float(precio_str.split()[0])
            cantidad = int(self.entry_cantidad_venta.get())
            total = precio * cantidad
            messagebox.showinfo("Venta Realizada", f"Venta realizada. Total: {total} MXN")
            self.entry_cantidad_venta.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor selecciona un producto para realizar la venta.")
    
if __name__ == "__main__":
    app = RestauranteApp()
    app.minsize(450, 400)
    app.mainloop()