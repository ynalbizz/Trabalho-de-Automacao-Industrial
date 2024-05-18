from EspCodes import *

Devices = [Device("ventilador", "192.168.0.106")]


def onehandcontroller(hand, fingers, clampfingersdist, handpos, areas):

    # Delimita a detecção dos gestos referente a mão direita
    if hand == "Right":
        # Adiciona lógica para ligar o LED quando o gesto for detectado
        if fingers == [0, 1, 0, 0, 0]:
            print("Rg1")

        if fingers == [0, 1, 1, 0, 0]:
            # c.write(b'A')
            print("Rg2")

    for area in areas:
        arearesult = area.execute(handpos)
        if arearesult[1]:
            for device in Devices:
                if device.name() == arearesult[0]:
                    if fingers == [0, 1, 0, 0, 0]:
                        device._ToggleState()


    # Delimita a detecção dos gestos referente a mão esquerda
    if hand == "Left":
        # Adiciona lógica para desligar o LED quando o gesto for detectado
        if fingers == [0, 1, 0, 0, 0]:
            # c.write(b'K')
            print("Lg1")

        if fingers == [0, 1, 1, 0, 0]:
            # c.write(b'B')
            print("Lg2")
        

def twohandcontroller(distbetweenhands):

    # Adiciona novos gestos Exclusivos para Duas
    if distbetweenhands >= 100:
        print("maior que 10cm")
