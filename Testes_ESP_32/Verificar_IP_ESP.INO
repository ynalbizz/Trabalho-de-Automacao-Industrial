#include <WiFi.h>

const char* ssid = "Colocar nome da rede aqui"; // SSID da sua rede Wi-Fi
const char* password = "senha da rede aqui"; // Senha da sua rede Wi-Fi

void setup() {
  delay(1000); // Aguarda 1 segundo para garantir que o ESP32 tenha tempo suficiente para inicializar completamente
  Serial.begin(9600);

  Serial.println();
  Serial.println("Conectando-se à rede Wi-Fi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Conectado à rede Wi-Fi");
  Serial.print("IP do ESP32: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Não há nada no loop porque queremos apenas imprimir o endereço IP uma vez
}
