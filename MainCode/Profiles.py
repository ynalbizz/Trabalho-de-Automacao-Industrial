from Devices import Device
from Areas import *

#Lista de Dispositivos:
#ventilador = Device("192.168.0.106","Ventilador")


#lista de Areas
#Area("Area1",(50, 50), 200, 100, ventilador)
#Area("Area2",(200,200), 100, 100)
currentProfile = 0

def _setProfile(n):
    global currentProfile
    areasList.clear()

    if n == 1:
        Area("Area1", (50, 50), 200, 100)


    if n == 2:
        Area("Area1", (200, 200), 150, 150)

    if n == 3:
        Area("Area1", (200, 200), 500, 500)


    currentProfile = n