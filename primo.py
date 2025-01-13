def es_primo(num):
    contador = True
    if num < 2:
        print("No es un numero valido")
        contador = False
    for i in range (2,int(num**0.5) + 1):
        print(i)
        if num % i == 0:
            contador = False
            
            break
    return contador


while True:
    try:
        numero = int(input("Ingresa un número entero positivo: ")) 
    except:
        input(f" Es una letra \n")
    else:
        break
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


"""def es_primo(num):
    contador = True
    for i in range (2,num):
        if num % i == 0:
            contador = False
    return contador

numero = input("Ingresa un número entero positivo: ")

print(es_primo(int(numero)))
"""