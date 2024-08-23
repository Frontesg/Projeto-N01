""" import pyautogui

pyautogui.click(1236,39,duration=0.5,button='right') """

import pyautogui
import keyboard
from PIL import ImageGrab
import time
import pytesseract as pyt
import cv2


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

    imagem = cv2.imread("screenshot.png")
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    texto = pyt.image_to_string(imagem, lang="por")
    textoT1 = texto.find('<')
    textoT2 = texto[textoT1+1:].split()
    textoT3 = textoT2[0]

    
    print('Mapa: '+ textoT3)

# Função que guarda o atalho Ctrl + X
def listen_for_screenshot():
    print("Pressione Ctrl + X para capturar o screenshot.")
    while True:
        if keyboard.is_pressed('ctrl+x'):
            capture_screenshot_around_mouse()
            time.sleep(1)  # Evita múltiplos prints

# Inicia a escuta do atalho de teclado
listen_for_screenshot()