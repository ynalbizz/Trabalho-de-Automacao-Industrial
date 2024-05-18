
//Este codigo esta em liguagem arduino e utilizarei a arduino ide para subir para o ESP

#include <WiFi.h>

const char* ssid = "GTDAS";      // SSID da sua rede Wi-Fi
const char* password = "novotempo"; // Senha da sua rede Wi-Fi

WiFiServer server(1234);  // Cria um servidor na porta 1234

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  
  // Conecta-se à rede Wi-Fi
  Serial.println();
  Serial.println("Conectando à rede Wi-Fi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Conectado à rede Wi-Fi");
  
  // Inicia o servidor
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (!client) {
    return;
  }

  // Aguarda a conexão do cliente
  Serial.println("Novo cliente conectado");
  
  while (client.connected()) {
    if (client.available()) {
      String comando = client.readStringUntil('\n');
      comando.trim();

      // Executa o comando recebido
      if (comando == "ligar") {
        digitalWrite(LED_BUILTIN, HIGH); // Acende o LED
        client.println("LED ligado");
      } else if (comando == "desligar") {
        digitalWrite(LED_BUILTIN, LOW); // Desliga o LED
        client.println("LED desligado");
      } else {
        client.println("Comando inválido");
      }
    }
  }

  // Fecha a conexão
  client.stop();
  Serial.println("Cliente desconectado");
}