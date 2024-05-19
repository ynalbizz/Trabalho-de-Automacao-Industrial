import cv2
import matplotlib.pyplot as plt
import socket
import time

# Initial setup
port = 1234

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


class Device:
    def __init__(self, ip, cooldown=5):
        # name the device
        # create a socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cooldown = cooldown  # cooldown in seconds
        self.last_toggle_time = 0  # time of the last state change

        # try to connect to the device
        try:
            print(ip)
            self.socket.connect((ip, port))
            self.socket.send("statecheck".encode())
            self.state = ('ligado' == self.socket.recv(1024).decode())
        except Exception as e:
            print("Dispositivo ({}) Ip:({}) Falhou!! \nErro: \n {}".format(device, ip, e))

    def _ToggleState(self):
        current_time = time.time()
        if current_time - self.last_toggle_time < self.cooldown:
            print(f"Cooldown ativo. Aguarde {self.cooldown - (current_time - self.last_toggle_time):.2f} segundos.")
            return

        if self.state:
            self.socket.send("desligar".encode())
        else:
            self.socket.send("ligar".encode())

        self.state = not self.state
        self.last_toggle_time = current_time
