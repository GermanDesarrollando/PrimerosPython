'''medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')
medios_transporte.pop(3)

print(medios_transporte)

lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("mala","buena"))

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print("buena" in frase)

mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion' : 'Periodista'}

print(mi_dic["nombre"])

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}} 
print(mi_dict['puntos']["points2"][1])



z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1
'''
from random import randint

nombre = input("Cual es tu nombre?\n")
print(f"Hola {nombre}, estoy pensando un numero entre 0 y 100")
numero = randint(0,100)
for indice, i in enumerate(range (7,0,-1)):
    intento = int(input())
    if intento == numero:
        print(f"Felicidades {intento} es el numero secreto, lo adivinaste en {indice} intentos")
        break
    if intento <= numero:
        print(f"El numero es mayor que {intento}, te quedan {i} intentos")
    elif intento >= numero:
        print(f"El numero es menor que {intento}, te quedan {i} intentos")
    
