def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        #caso recursivo
        #pasi 1: mueve la torre mas pequena de origen a auxiliar
        torres_hanoi(n - 1, origen, auxiliar, destino)

        #paso 2: mueve el disco mas grande de origen a destino
        print(f"Mover disco {n} de {origen} a {destino}")

        #paso 3: mueve la torre de auxiliar a destino, utilizando otigen como auxiliar
        torres_hanoi(n - 1, auxiliar, destino, origen)


#ejemplo de uso con 3 discos de A a C usando b como auxiliar     
torres_hanoi(4, "A", "B", "C")