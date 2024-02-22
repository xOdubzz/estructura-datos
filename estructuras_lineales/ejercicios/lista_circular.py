class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_al_principio(self, dato):
        nuevo_nodo = NodoCircular(dato)
        if not self.cabeza:
            nuevo_nodo.siguiente = nuevo_nodo
            #hacerlo apuntaer a si mismo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza.siguiente
            self.cabeza.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        if not actual:
            print("Lista vacia")
            return
        while True:
            print(actual.dato, end= " ->")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("...(Continua ciclicamente)")


lista = ListaCircular()
lista.agregar_al_principio(3)
lista.agregar_al_principio(2)
lista.agregar_al_principio(1)
lista.imprimir_lista()