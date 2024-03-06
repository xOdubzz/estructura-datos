import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class NodoListaEnlazada():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

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

class ColarCircular():
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

class RestauranteApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación de Restaurante")
        self.tabControl = ttk.Notebook(self)

        self.tabEmpleados = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabEmpleados, text="Empleados")

        self.tabTurnos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabTurnos, text="Turnos")

        self.tabOrdenes = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabOrdenes, text="Órdenes")

        self.tabHistorial = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabHistorial, text="Historial")

        self.tabReservas = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabReservas, text="Reservas")

        # Acomodar Pestañas
        self.tabControl.pack(expand=1, fill="both")

        # Definir la lista enlazada de empleados
        self.lista_empleados = ListaEnlazada()

        #definir la cola circular de turnos
        self.cola_turnos = ColarCircular()

        # Llamar metodos para definir Pestañas
        self.create_empleados_widgets()
        self.create_turnos_widgets()
        self.create_ordenes_widgets()
        self.create_historial_widgets()
        self.create_reservas_widgets()

        

    def create_empleados_widgets(self):

        # Pestaña Empleados
        # Crear un Frame para los widgets de empleados
        frame_empleados = ttk.LabelFrame(self.tabEmpleados, text="Gestión de Empleados - USANDO LISTAS ENLAZADAS")
        frame_empleados.pack(padx=10, pady=10, fill="both", expand=True)

        # Etiqueta y entrada para el nombre del empleado
        lbl_nombre = tk.Label(frame_empleados, text="Nombre:")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_empleados)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Botón para agregar un nuevo empleado
        btn_agregar = tk.Button(frame_empleados, text="Agregar Empleado", command=self.agregar_empleado)
        btn_agregar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

         # Crear un Listbox para mostrar los empleados
        self.listbox_empleados = tk.Listbox(frame_empleados)
        self.listbox_empleados.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        btn_editar = tk.Button(frame_empleados, text="Editar emppleado", command=self.editar_empleados)
        btn_editar.grid(row=3, column=0, columnspan=2, padx=5, pady= 5)

        btn_eliminar = tk.Button(frame_empleados, text= "Eliminar empleado", command=self.eliminar_empleado)
        btn_eliminar.grid(row=3, column=3, columnspan=2, padx=5, pady=5)


    def agregar_empleado(self):
        # Obtener el nombre del empleado ingresado en la entrada
        nombre_empleado = self.entry_nombre.get()

        # Verificar si se ingresó un nombre
        if nombre_empleado:
            # Crear un nuevo nodo con el nombre del empleado
            #nuevo_empleado = NodoListaEnlazada(nombre_empleado)
            
            # Agregar el nuevo empleado a la lista enlazada de empleados
            self.lista_empleados.agregar_al_principio(nombre_empleado.upper())
            
            # Actualizar la visualización de la lista de empleados
            self.actualizar_lista_empleados()


            # Limpiar la entrada después de agregar el empleado
            self.entry_nombre.delete(0, tk.END)

            self.lista_empleados.mostrar_lista()

            empleados = []
            empleados.append(self.lista_empleados.mostrar_lista())

            messagebox.showinfo("Infor","Guardado exitosamente")


        else:
            # Mostrar un mensaje de error si no se ingresó un nombre
            messagebox.showerror("Error", "Por favor ingresa el nombre del empleado.")

    def actualizar_lista_empleados(self):
        # Limpiar el contenido actual del Listbox
        self.listbox_empleados.delete(0, tk.END)
        
        # Obtener la lista de empleados y agregarlos al Listbox
        empleados = self.lista_empleados.obtener_lista()
        for empleado in empleados:
            self.listbox_empleados.insert(tk.END, empleado)

    def editar_empleados(self):
        #se necesita obtener el indice del empleado
        seleccionado = self.listbox_empleados.curselection()

        if seleccionado:

            indice = seleccionado[0]

            #obtener valor del empleado en la lista

            empleado_seleccionado = self.listbox_empleados.get(indice)

            #crear una ventana emergente para editar

            ventana_edicion = tk.Toplevel(self)
            ventana_edicion.title("Editar empleados")
            
            #entrada para sustituir valor
            lbl_nuevo_valor = tk.Label(ventana_edicion, text = "Nuevo valor: ")
            lbl_nuevo_valor.grid(row=0, column=0, padx=5, pady= 5)

            entry_nuevo = tk.Entry(ventana_edicion)
            entry_nuevo.grid(row=0, column=1, padx=5, pady=5)

            #boton para guardar cambios

            btn_confirmar = tk.Button(ventana_edicion, text= "Guardar cambios", command= lambda: self.confirmar_edicion(indice, entry_nuevo.get(), ventana_edicion))
            btn_confirmar.grid(row=1, column=0, columnspan= 2)

        else:
            #mostrar mensaje de error sino se selecciono un elemento de la lista
            messagebox.showerror("ERROR", "Debe seleccionar un empleado")

    def confirmar_edicion(self, indice, nuevo_valor, ventana_edicion):
            
        #actualizar el valor seleccionado
        empleados = self.lista_empleados.obtener_lista()
        empleados[indice] = nuevo_valor.upper()

        self.lista_empleados = ListaEnlazada()
        for empleado in empleados:
            self.lista_empleados.agregar_al_principio(empleado)
        
        #actualizar lista de empleados
        self.actualizar_lista_empleados()

        # una vez realizado este proceso, se debe cerrar la ventana

        ventana_edicion.destroy()

    def eliminar_empleado(self):

        selfeccionado = self.listbox_empleados.curselection()

        if selfeccionado:

            indice = selfeccionado[0]
            empleado_borrar = self.listbox_empleados.get(indice)

            respuesta = messagebox.askyesno("Confirmar Eliminacion", f"Estas seguro de eliminar este elemento? \n {empleado_borrar}")

            if respuesta:
                #en este caso se elimina el registro
                empleados = self.lista_empleados.obtener_lista()
                del empleados[indice]

            # 
            
            self.lista_empleados = ListaEnlazada()

            for empleado in empleados:
                self.lista_empleados.agregar_al_principio(empleados)
            
            self.actualizar_lista_empleados()

            messagebox.showinfo("Info", "Eliminado exitosamente")

    def create_turnos_widgets(self):
        #pestana de turnos
        frame_turnos = ttk.Frame(self.tabTurnos)
        frame_turnos.pack(fill="both", expand=True)

        lbl_turno = tk.Label(frame_turnos, text= "Turno: ")
        lbl_turno.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.entry_turno = tk.Entry(frame_turnos)
        self.entry_turno.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_asignar_turno = tk.Button(frame_turnos, text="Asignar Turno", command=self.asignar_turno)
        btn_asignar_turno.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        btn_avanzar_turno = tk.Button(frame_turnos, text="Avanzar turno", command=self.avanzar_turno)
        btn_avanzar_turno.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_turnos = tk.Listbox(frame_turnos)
        self.listbox_turnos.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def asignar_turno(self):
        turno = self.entry_turno.get()
        if turno:
            empleado = self.lista_empleados.obtener_lista().pop()
            self.cola_turnos.encolar((empleado, turno))
            self.actualizar_lista_turnos()
            self.entry_turno.delete(0, tk.END)
            messagebox.showinfo("Informacion", f"turno {turno} asignado a {empleado}.")

        else:
            messagebox.showerror("Error", "Por favor, ingresa el turno.")


    def avanzar_turno(self):
        if not self.cola_turnos.esta_vacia():
            empleado, turno = self. cola_turnos.desencolar()
            self.cola_turnos.avanzar_turno()
            self.actuaizar_lista_turnos()
            messagebox.showinfo("Informacion", f"Avanzado al siguiente turno: {turno}.")

    def actualizar_lista_turnos(self):
        self.listbox_turnos.delete(0, tk.END)
        turnos = [f"{empleado}: {turno}" for empleado, turno in self.cola_turnos.items]
        for turno in turnos:
            self.listbox_turnos.insert(tk.END, turno)

    def create_ordenes_widgets(self):
        # Aquí crearías los widgets para la pestaña de órdenes
        pass

    def create_historial_widgets(self):
        # Aquí crearías los widgets para la pestaña de historial
        pass

    def create_reservas_widgets(self):
        # Aquí crearías los widgets para la pestaña de reservas
        pass


if __name__ == "__main__":
    app = RestauranteApp()
    app.minsize(380, 400)
    app.mainloop()
