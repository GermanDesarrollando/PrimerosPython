def es_palindromo(texto):
    texto = texto.lower().replace(" ","").replace(",","")
    print(texto)
    return texto == texto[::-1]
       
texto = input("Introduce un texto:")

if es_palindromo(texto):
    print(f"{texto}, es un palindromo")
else:
    print(f"{texto}, no es un palindromo")

"""def es_palindromo(texto):
    texto.lower()
    texto = list(texto)
    #texto.remove(',')
    texto.remove(' ')
    texto_invertido = texto
    texto_invertido.reverse()
    for l, n in zip(texto,texto_invertido):
        if l != n:
            return False
    return True
texto = input("Introduce un texto:")
es_palindromo(texto)

if es_palindromo:
    print(f"{texto}, es un palindromo")
else:
    print(f"{texto}, no es un palindromo")"""