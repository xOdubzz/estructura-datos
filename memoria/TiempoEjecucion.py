#medir tiempo de ejecicion de algoritmos python

import time

#algoritmo 1 - bubble sort

start_time = time.time()

def bubble_sort(arr):
    n = len(arr)
    for i in range (n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#ejemplo de uso
lista_desordenada1 = [64, 34, 25, 12 ,22, 11, 90]

bubble_sort(lista_desordenada1)

print("La lista ordenada  con bubble sort es: ", lista_desordenada1)




tiempo_de_ejecucion_final = float(time.time() - start_time)

print(f"Tiempo de ejecucion del algoritmo 1: {tiempo_de_ejecucion_final} segundos")



#algoritmo2 quicksort

start_time2 = time.time()

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in  arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#ejemplo de uso

lista_desordenada2 = [64, 34, 25, 12 ,22, 11, 90]
resultado = quicksort(lista_desordenada2)
print("Lista ordenada usando quicksort: ", resultado)

tiempo_de_ejecucion_final2 = float(time.time() - start_time2)
print(f"Tiempo de ejecucion del algoritmo 2 : {tiempo_de_ejecucion_final2} segundos")