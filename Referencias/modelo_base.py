import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import serial
from time import sleep

# Inicializa a porta serial com uma taxa de transmissão de 9600 baud
c = serial.Serial('COM3', 9600)
sleep(5)  # Aguarda 5 segundos para garantir a inicialização completa

video = cv2.VideoCapture(0)
video.set(3, 1280)
video.set(4, 720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)
estadoAtual = [0, 0, 0, 0, 0]

setaDir = cv2.imread('seta dir.PNG')
setaEsq = cv2.imread('seta esq.PNG')

while True:
    _, img = video.read()
    hands, img = detector.findHands(img)

    if hands:
        estado = detector.fingersUp(hands[0])
        print(estado)

        if estado != estadoAtual and estado == [0, 0, 0, 0, 1]:
            print('passar slide')
            kb.press(Key.right)
            kb.release(Key.right)
            # Adiciona lógica para ligar o LED quando o gesto for detectado
            c.write(b'L')

        elif estado != estadoAtual and estado == [1, 0, 0, 0, 0]:
            print('voltar slide')
            kb.press(Key.left)
            kb.release(Key.left)
            # Adiciona lógica para desligar o LED quando o gesto for detectado
            c.write(b'K')

        estadoAtual = estado

    cv2.imshow('img', cv2.resize(img, (640, 420)))
    cv2.waitKey(1)