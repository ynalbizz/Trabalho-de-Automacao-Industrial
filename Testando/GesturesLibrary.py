import AuxiliarLibrary as Aux
import socket

# Endereço IP do ESP32 e porta
ESP_IP = "192.168.0.102"  # Coloque o endereço IP do seu ESP32 aqui (Temos um codigo que verifica para voce)
PORT = 1234  # Escolha uma porta disponível

# Cria o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao ESP32
client_socket.connect((ESP_IP, PORT))
s1 = Aux.OnOffSwitch()
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
        try:

            arearesult = area.execute(handpos)
            if arearesult[2]:
                if fingers == [0, 1, 0, 0, 0]:
                    client_socket.send("ligar".encode())
                    resposta = client_socket.recv(1024).decode()
                    print("Resposta do ESP32:", resposta)
                if fingers == [0, 1, 0, 0, 0]:
                    client_socket.send("ligar".encode())
                    resposta = client_socket.recv(1024).decode()
                    print("Resposta do ESP32:", resposta)










        except Exception as erro:
            print(erro)

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
