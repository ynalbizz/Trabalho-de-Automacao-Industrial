import time

# Variável para controlar o estado do interruptor (ligado/desligado)
interruptor_ligado = False

# Variável para controlar o último momento em que o interruptor foi usado
ultimo_uso = 0

# Função para ligar o interruptor
def ligar_interruptor():
    global interruptor_ligado, ultimo_uso
    if time.time() - ultimo_uso >= 10:  # Verifica se já passou o cooldown
        interruptor_ligado = True
        ultimo_uso = time.time()
        print("Interruptor ligado.")
    else:
        print("Aguarde 10 segundos para usar o interruptor novamente.")

# Função para desligar o interruptor
def desligar_interruptor():
    global interruptor_ligado
    interruptor_ligado = False
    print("Interruptor desligado.")

# Teste do interruptor
ligar_interruptor()
print("Estado do interruptor:", "ligado" if interruptor_ligado else "desligado")
time.sleep(5)  # Espera 5 segundos
ligar_interruptor()  # Tenta ligar o interruptor antes do cooldown acabar
print("Estado do interruptor:", "ligado" if interruptor_ligado else "desligado")
time.sleep(6)  # Espera mais 6 segundos
ligar_interruptor()  # Deve conseguir ligar o interruptor após o cooldown
print("Estado do interruptor:", "ligado" if interruptor_ligado else "desligado")
