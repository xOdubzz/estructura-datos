def conteo_digitos(digito):

    if digito < 10:
        return 1
    else:
        return 1 + conteo_digitos(digito / 10)
    
resultado = conteo_digitos(233)
print(resultado)