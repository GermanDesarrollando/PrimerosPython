"""def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    palabra1 = palabra1.strip()
    palabra2 = palabra2.strip()
    lista1 = list(palabra1)
    lista2 = list(palabra2)
    lista1.sort()
    lista2.sort()
    if len(lista1) == len(lista2):
        for l, m in zip(lista1,lista2):
            if l != m:
                return False
        return True 
    return False
palabra1 = input("Ingresa un palabra:\n")
palabra2 = input("Ingresa otra palabra:\n")

if son_anagramas(palabra1, palabra2):
    print(f"es un anagrama.")
else:
    print(f"no es un anagrama.")

"""

def son_anagramas(palabra1, palabra2):
    # Normalizar: convertir a minúsculas y eliminar espacios
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    # Comparar las palabras ordenadas
    return sorted(palabra1) == sorted(palabra2)

# Pedir las palabras al usuario
palabra1 = input("Ingresa una palabra:\n")
palabra2 = input("Ingresa otra palabra:\n")

# Comprobar si son anagramas
if son_anagramas(palabra1, palabra2):
    print(f'"{palabra1}" y "{palabra2}" son anagramas.')
else:
    print(f'"{palabra1}" y "{palabra2}" no son anagramas.')

