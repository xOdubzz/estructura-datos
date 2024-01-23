#ejemplo de uso de memoria dinamica usando clases

#definicion de la clase
class ListaDinamica:
    def __init__(self):
        self.elementos = []

    def agregarElementos(self, elemento):
        self.elementos.append(elemento)

    def mostrarElementos(self):
        print("Elementos de la lista: ", self.elementos)

#metodo para usar la ListaDinamica
def uso_memoria_dinamica():
    new_lista = ListaDinamica() #objeto tipo lista dinamica

    new_lista.agregarElementos(10)
    new_lista.agregarElementos(10)

    new_lista.mostrarElementos()

if __name__ == "__main__":
    uso_memoria_dinamica()

