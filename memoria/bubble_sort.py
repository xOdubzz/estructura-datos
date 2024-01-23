def bubble_sort(arr):
    n = len(arr)
    for i in range (n - 1):
        for j in range(0, n - i - 1):
            print(arr[i],arr[j])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

lista_desordenada = [64, 34, 25, 12 ,22, 11, 90]

bubble_sort(lista_desordenada)

print("La lista ordenada  con bubble sort es: ", lista_desordenada)