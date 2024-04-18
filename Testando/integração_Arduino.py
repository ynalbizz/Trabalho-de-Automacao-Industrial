from pynput.keyboard import Key, Controller
import serial
from time import sleep#delay for communication

#Inicializa a porta serial com uma taxa de transmissão de 9600 baud
serial.Serial('COM3', 9600)
sleep(5)  
