# def ejemplo_recursivo(n):
#     #caso base
#     if n == 0:
#         return 0
#     #llamada recursiva
#     else:
#         return n + ejemplo_recursivo(n - 1)
    
# resultado = ejemplo_recursivo(5)
# print(f"Resultado es: {resultado}")


# def factorial(n):
#     print(n)
#     if n == 0 or n == 1:
#         print(n)
#         return 1
#     else:
#         print("aqui")
#         return n * factorial(n - 1)

# resultado = factorial(5)
# print(f"Resultado: {resultado}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)
    
resultado = fibonacci(9)
print(f"Resultado: {resultado}")