import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import serial
from time import sleep#delay para comunicaçâo
estadoinicial = [0, 0, 0, 0, 0]
# Inicializa a porta serial com uma taxa de transmissão de 9600 baud
c = serial.Serial('COM3', 9600)#Caso altere a entrada, mudar porta de comunicação
sleep(5)  # Aguarda 5 segundos para garantir a inicialização completa


def gestos(mao,dedos):

    #Delimita a detecção dos gestos referente a mão direita
    if(mao == "Right"):

        # Adiciona lógica para ligar o LED quando o gesto for detectado
        if(dedos == [0, 1, 0, 0, 0]):
            c.write(b'L')
        if(dedos == [0, 1, 1, 0, 0]):
            c.write(b'A')
        

    #Delimita a detecção dos gestos referente a mão esquerda
    if(mao == "Left"):
        # Adiciona lógica para desligar o LED quando o gesto for detectado
        if (dedos == [0, 1, 0, 0, 0]):
            c.write(b'K')
        if (dedos == [0, 1, 1, 0, 0]):
            c.write(b'B')
    
video = cv2.VideoCapture(0)
video.set(3, 1280)
video.set(4, 720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)

while True:
    _, img = video.read()
    hands, img = detector.findHands(img)

    if hands:
        # Vê se a primeira mão esta Levantada e define quais Atributos da mão seram usado no codigo
        hand1 = hands[0]  
        mao1 = hand1["type"]
        dedos1 = detector.fingersUp(hand1)
        gestos(mao1,dedos1)

        # Vê se a segunda mão esta Levantada
        if len(hands) == 2:
            #Define quais Atributos da mão seram usado no codigo
            hand2 = hands[1]
            mao2 = hand2["type"]
            dedos2 = detector.fingersUp(hand2)
            gestos(mao2,dedos2)
            



    print("")
    cv2.imshow('img', cv2.resize(img, (640, 420)))
    cv2.waitKey(1)