import cv2


def printinfos(variabels):
    print(variabels)


def handlocationverifiying(handPos, area):

    origin = area["origin"]
    end = area["end"]
    if origin[0] <= handPos[0] <= end[0] and origin[1] <= handPos[1] <= end[1]:
        return True


class Area:
    def __init__(self, centerpos, width, height, img, action):
        self.img = img
        self.width = width
        self.height = height
        self.centerpos = centerpos
        origin = (centerpos[0]-width, centerpos[1]-height)
        end = (centerpos[0]+width, centerpos[1]+height)
        self.origin = origin
        self.end = end
        self.action = action

    def infos(self, info="all"):

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
            return infos[info]

    def drawArea(self):
        colorr = (255, 0, 255)
        cv2.rectangle(self.img, self.origin, self.end, colorr, 2)

    def _isHandInside(self, handPos):
        return self.origin[0] <= handPos[0] <= self.end[0] and self.origin[1] <= handPos[1] <= self.end[1]

    def execute(self, handPos):
        if self._isHandInside(handPos):
            self.action()



