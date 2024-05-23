import CamCode
import GesturesLibrary as GestLib
import Profiles

Profiles._setProfile(1)
while True:
    handtrackinginfos, distanceBetweenHands = next(CamCode._GetHandsInfo())
    GestLib.controller(handtrackinginfos,distanceBetweenHands)

