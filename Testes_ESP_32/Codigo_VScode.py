import socket

# Endereço IP do ESP32 e porta
ESP_IP = "192.168.0.110"  # Coloque o endereço IP do seu ESP32 aqui (Temos um codigo que verifica para voce)
PORT = 1234  # Escolha uma porta disponível

# Cria o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao ESP32
client_socket.connect((ESP_IP, PORT))

while True:
    # Solicita ao usuário que digite o comando
    comando = input("Digite 'ligar' para ligar o LED ou 'desligar' para desligar o LED: ").lower()
    
    # Envia o comando para o ESP32
    client_socket.send(comando.encode())

    # Aguarda a resposta do ESP32
    resposta = client_socket.recv(1024).decode()
    print("Resposta do ESP32:", resposta)

# Fecha o socket
client_socket.close()