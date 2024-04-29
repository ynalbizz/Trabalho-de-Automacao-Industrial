import numpy as np
import cvzone
import cv2
import pprint

def HandLocationVerifiying(handPos,area):

    origin = area["origin"]
    end = area["end"]
    if origin[0] <= handPos[0] <= end[0] and origin[1] <= handPos[1] <= end[1]:
       return True
   
   


class Area:
    def __init__(self,centerpos,width,height,img):
        self.img = img
        self.width = width
        self.height = height
        self.centerpos = centerpos
        origin = (centerpos[0]-width,centerpos[1]-height)
        end =(centerpos[0]+width,centerpos[1]+height)
        self.origin = origin
        self.end = end

    def Infos(self, info="all"):

        infos = {
         "origin": self.origin,
         "end": self.end,
         "width": self.width,
         "height": self.height,
         "centerpos": self.centerpos
        }
        if info == "all":
            return infos
        else:
            return(infos(info))

    def DrawArea(self):
        
        colorR=(255, 0, 255)
        cv2.rectangle(self.img,self.origin,self.end,colorR,2)
 

