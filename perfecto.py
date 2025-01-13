def es_perfecto(numero):
    contador = 1
    for i in range(2,int(numero/2)+1):
        if numero % i == 0:
            contador += i
    if contador == numero and contador > 1:
        return True    
    else:
        return False

# Ciclo para pedir al usuario un número válido
while True:
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        if numero < 0:
            raise ValueError("El número debe ser positivo.")
    except ValueError as e:
        print(f"Entrada no válida: {e}")
    else:
        break  # Salir del ciclo si la entrada es válida

if es_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")