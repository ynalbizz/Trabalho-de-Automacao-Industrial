import cv2
import matplotlib.pyplot as plt
import time

# Initial setup


class Area:
    def __init__(self, centerpos, width, height, img, device):
        self.img = img
        self.width = width
        self.height = height
        self.centerpos = centerpos
        origin = (centerpos[0]-width, centerpos[1]-height)
        end = (centerpos[0]+width, centerpos[1]+height)
        self.origin = origin
        self.end = end
        self.device = device

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
            return self.device, self._isHandInside(handPos)


class Graph:
    def __init__(self, title):
        self.fig, self.ax = plt.subplots(facecolor="#eeeee4")
        self.times = []
        self.ydata = []
        (self.start_time, self.line) = (time.time(), self.ax.plot(self.times, self.ydata, 'r')[0])

        self.fig.suptitle(title)

    def plotGraph_Y_byTime(self, y):

        if y:
            current_time = time.time() - self.start_time  # Time elapsed since start
            self.times.append(current_time)
            self.ydata.append(y)

            self.line.set_xdata(self.times)
            self.line.set_ydata(self.ydata)

            self.ax.relim()  # Recalculate limits
            self.ax.autoscale_view(True, True, True)  # Rescale axis to fit data
            plt.draw()  # Redraw the current figure
            plt.pause(0.1)

            return
    plt.pause(0.1)
