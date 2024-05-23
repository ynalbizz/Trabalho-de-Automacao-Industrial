import socket
import time

# Initial setup
port = 1234
global devicesList
devicesList = {}

class Device:
    def __init__(self, ip, name=None, cooldown=5):
        # name the device
        # create a socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cooldown = cooldown  # cooldown in seconds
        self.last_toggle_time = 0  # time of the last state change
        self.name = name

        # try to connect to the device
        try:
            self.socket.connect((ip, port))
            self.socket.send("statecheck".encode())
            self.state = ('ligado' == self.socket.recv(1024).decode())
        except Exception as e:
            self.state = None
            print("Dispositivo ({}) Ip:({}) Falhou!! \nErro: \n {}".format(name, ip, e))

        devicesList[self.name] = self

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
