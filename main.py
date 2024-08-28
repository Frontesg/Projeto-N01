
from models.connection_options.connection import DBConnectionHandler
from models.repository.mapa_info_repository.mapInfo_repository import MapInfoRepository
import pyautogui
import keyboard
from PIL import ImageGrab
import time
import pytesseract as pyt
import cv2

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

peipou = MapInfoRepository(db_connection)

# Função para capturar a tela
def capture_screenshot_around_mouse(region_size=250):
    # Obtém a posição atual do mouse
    x, y = pyautogui.position()

    # coordenadas
    left = x - region_size // 1
    top = y - region_size // 3.5
    right = x # + region_size // 1
    bottom = y # + region_size // 2

    # Captura a região da tela em volta do mouse
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Salva o screenshot.
    screenshot.save(f"screenshot.png")

    imagem = cv2.imread("screenshot1.png")
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    texto = pyt.image_to_string(imagem, lang="por")
    textoT1 = texto.find('<')
    textoT2 = texto[textoT1+1:].split()
    textoT3 = textoT2[0]
    print(textoT3)
    resposta = peipou.select_one(textoT3)
    print(resposta)


# Função que guarda o atalho Ctrl + X
def listen_for_screenshot():
    print("Pressione Ctrl + X para capturar o screenshot.")
    while True:
        if keyboard.is_pressed('ctrl+x'):
            capture_screenshot_around_mouse()
            time.sleep(1)  # Evita múltiplos prints

# Inicia a escuta do atalho de teclado
listen_for_screenshot()