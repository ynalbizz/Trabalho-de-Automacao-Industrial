from Areas import areasList
import Profiles

def controller(hands,distbetweenhands):
    for hand in hands:
        if Profiles.currentProfile == 2:
            if areasList['Area1']._isHandInside(hand['center']):
                print('vc é incrivel')

            # Delimita a detecção dos gestos referente a mão direita
            if hand['type'] == "Right":
                # Execulta ação quando gesto for detectado
                if hand['fingers'] == [0, 1, 0, 0, 0]:
                    print("Right Gesture 1")
                    Profiles._setProfile(2)

            # Delimita a detecção dos gestos referente a mão esquerda
            if hand['type']  == "Left":
                # Execulta ação quando gesto for detectado
                if hand['fingers'] == [0, 1, 0, 0, 0]:
                    # c.write(b'K')
                    print("Left Gesture 1")
                    Profiles._setProfile(3)


    if distbetweenhands != None and distbetweenhands >= 10:
        print("maior que 10cm")
