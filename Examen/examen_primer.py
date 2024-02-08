import time

def invertir_palabra(palabra):
    if len(palabra) <= 1:
        return palabra
    else:
        return palabra[-1] + invertir_palabra(palabra[1:-1]) + palabra[0]
    

def palindromo(muestra, resultado):
    if muestra == resultado:
        print (f"La palabra es un palindromo")
    else:
        print (f"La palabra no es un palindromo")

def funcion_normal():

    pala = input("Ingresa la palabra para testear si es palindromo o no: ")
    resultado = invertir_palabra(pala)
    
    test = palindromo(pala, resultado)

def funcion():

    pala = input("Ingresa la palabra para testear si es palindromo o no: ")
    start_time = time.time()
    resultado = invertir_palabra(pala)
    
    test = palindromo(pala, resultado)
    tiempo_de_ejecucion_final = float(time.time() - start_time)
    print(f"El tiempo de ejecucion de la funcion es de {tiempo_de_ejecucion_final}")


print("MENU: ")
print("1.- Programa Palindromo")
print("2.- Medir tiempo de Ejecucion del Alforitmo Recursivo")
print("3.- Salir")


while True:
    eleccion = int(input("Seleccione la opcion 1, 2, 3: "))

    if eleccion == 1:
        funcion_normal()
    elif eleccion == 2:
        funcion()
    elif eleccion == 3:
        break
    else:
        print("Opcion invalida")