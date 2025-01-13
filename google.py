from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Ruta al ChromeDriver
chrome_driver_path = "C:/Users/fgpatino/Downloads/chromedriver-win64/chromedriver.exe"

# Configura el servicio con la ruta del ChromeDriver
service = Service(chrome_driver_path)

# Inicia el navegador Chrome
driver = webdriver.Chrome(service=service)

# Abre una página web
driver.get("https://web.whatsapp.com")

# Tiempo para escanear el código QR
print("Escanea el código QR y presiona Enter.")
input()

# Lista de números con código de país y mensajes
contactos = ["+59176801799", "+59176801799"]  # Reemplaza con tus números
mensaje = "Hola, este es un mensaje automático."

for numero in contactos:
    # Abre la conversación con el número
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje}"
    driver.get(url)
    time.sleep(10)  # Esperar a que cargue el chat

    # Envía el mensaje
    enviar_btn = driver.find_element(By.XPATH, "//button[@data-testid='compose-btn-send']")
    enviar_btn.click()

    time.sleep(5)  # Esperar antes de pasar al siguiente contacto

# Cerrar el navegador
driver.quit()
