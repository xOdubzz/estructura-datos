def invertir_cadena_recursiva(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena_recursiva(cadena[1:-1]) + cadena[0]

resultado = invertir_cadena_recursiva("Hola")
print(resultado)
