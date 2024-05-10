import cv2
import matplotlib.pyplot as plt
import time
import socket




#Conecta ao ESP32

# Initial setup


def printinfos(variabels):
    print(variabels)


def handlocationverifiying(handPos, area):

    origin = area["origin"]
    end = area["end"]
    if origin[0] <= handPos[0] <= end[0] and origin[1] <= handPos[1] <= end[1]:
        return True


class Area:
    def __init__(self, centerpos, width, height, img, action,device):
        self.img = img
        self.width = width
        self.height = height
        self.centerpos = centerpos
        origin = (centerpos[0]-width, centerpos[1]-height)
        end = (centerpos[0]+width, centerpos[1]+height)
        self.origin = origin
        self.end = end
        self.action = action
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
        if self._isHandInside(handPos):
            return (str(self.action).lower(), self.device, True)


class Graph:
    def __init__(self,title):
        self.fig, self.ax = plt.subplots(facecolor=("#eeeee4"))
        self.times = []
        self.ydata = []
        (self.start_time, self.line) = (time.time(), self.ax.plot(self.times, self.ydata, 'r')[0])

        self.fig.suptitle(title)
    def plotGraph_Y_byTime(self,y):

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

class Dispositivo:
    def __init__(self,esp_ip,port,device_name):
        self.name = device_name
        self.ip = esp_ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((esp_ip,port))
    def infos(self):
        infos = {"ip": self.ip,"port": self.port,"name": self.name}

    def execute(self,command):
        self.client_socket.send(command.encode())