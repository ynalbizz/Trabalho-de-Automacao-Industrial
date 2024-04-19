from pynput.keyboard import Key, Controller
import serial
from time import sleep#delay for communication

# Inicializa a porta serial com uma taxa de transmissão de 9600 baud
c = serial.Serial('COM3', 9600)#Caso altere a entrada, mudar porta de comunicação
sleep(5)  # Aguarda 5 segundos para garantir a inicialização completa

