""" import pyautogui

pyautogui.click(1236,39,duration=0.5,button='right') """

import pyautogui
import keyboard
from PIL import ImageGrab
import time
import pytesseract as pyt
import cv2


# Função para capturar a tela ao redor do ponteiro do mouse
def capture_screenshot_around_mouse(region_size=250):
    # Obtém a posição atual do mouse
    x, y = pyautogui.position()

    # Calcula as coordenadas do retângulo em volta do mouse
    left = x - region_size // 1
    top = y - region_size // 3.5
    right = x # + region_size // 1
    bottom = y # + region_size // 2

    # Captura a região da tela em volta do mouse
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Salva o screenshot com um nome único
    #timestamp = int(time.time())
    screenshot.save(f"screenshot.png")

    imagem = cv2.imread("screenshot.png")
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    texto = pyt.image_to_string(imagem, lang="por")
    textoT1 = texto.find('<')
    textoT2 = texto[textoT1+1:].split()
    textoT3 = textoT2[0]

    
    print('Mapa: '+ textoT3)

    #print(f"Screenshot capturado e salvo como screenshot_{timestamp}.png")

# Função que aguarda o atalho Ctrl + X
def listen_for_screenshot():
    print("Pressione Ctrl + X para capturar o screenshot ao redor do mouse.")
    while True:
        if keyboard.is_pressed('ctrl+x'):
            capture_screenshot_around_mouse()
            time.sleep(1)  # Evita múltiplos prints com um único pressionamento de tecla

# Inicia a escuta do atalho de teclado
listen_for_screenshot()
'''
O

Estrada de Avalon para

<& Tynos-Eyexroi

2577 10239

XErFechoem 2h38m
'''