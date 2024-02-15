#Ejemplo simple de deshacer en un editor de texto

class EditorTexto:
    def __init__(self):
        #Aqui definimos la pila
        self.historial = []
    def agregar_texto(self, texto):
        #Utilizamos push para agreagar texto a la pila
        self.historial.append(texto)
    def deshacer(self):
        #utilizamos pop, pero antes validadndo que la pila no este vacia
        if self.historial:
            self.historial.pop()
    def mostrar_texto(self):
        return "".join(self.historial)
    
editor = EditorTexto()

editor.agregar_texto("Hola")
editor.agregar_texto(" Mundo")
print(editor.mostrar_texto())
editor.deshacer()
print(editor.mostrar_texto())