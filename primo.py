def es_primo(num):
    if num <= 1:  # Números menores o iguales a 1 no son primos
        return False
    for i in range(2, int(num**0.5) + 1):  # Revisar solo hasta la raíz cuadrada de num
        if num % i == 0:
            return False
    return True

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

# Mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
