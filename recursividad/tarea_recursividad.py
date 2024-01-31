# #suma de elementos de un array
 
# def suma_array(arr):

#     if len(arr) == 1:
#         # print(f"La suma de elementos es {arr[0]}")
#         return arr[0]
    
#     else:
#         i = 0
#         suma = arr[i] + arr[i + 1]
#         #print(f"La suma es: {suma}")
#         return suma + suma_array(arr)
#         i = i + 1

#         suma_array(arr)


def suma_array(arr):

    n = len(arr)

    if n == 1:
        return arr[0]
    else: 
        i = 0
        return arr[i] + arr[i + 1] 
    
        i = i + 1

    
    suma_array(arr)

#resultados = []
numeros = [1,2,3]

resultado = suma_array(numeros)
print(f"La suma de los elementos del array es: {resultado}")


