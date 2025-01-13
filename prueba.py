import pywhatkit

# Lista de números
numeros = ["+59176801799","+59176801799"]  # Incluye el código de país sin '+'
mensaje = "Hola, este es un mensaje automático."

for numero in numeros:
    pywhatkit.sendwhatmsg_instantly(f"+{numero}", mensaje, wait_time=15)