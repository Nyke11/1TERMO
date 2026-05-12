🌐 Arquitetura IoT I: Guia de Aula
Este documento é o seu mapa para entender como conectar o mundo físico ao digital. Vamos explorar o hardware, o firmware e a inteligência dos dados. 🚀

1. 🔌 O Ecossistema Arduino na IoT
O Arduino é a porta de entrada para a eletrônica. Na arquitetura IoT, ele geralmente ocupa a Camada de Percepção (Edge).

🛠️ Componentes Principais:
🧠 Microcontrolador: O processador central (ex: ATmega328P ou o potente ESP32 com Wi-Fi).

🔌 I/O (Inputs/Outputs): Pinos digitais e analógicos para "sentir" o mundo (sensores) e "agir" nele (atuadores).

💻 IDE Arduino: Onde a mágica da programação acontece.

2. ⚙️ Programação em C++ (O Coração do Hardware)
O C++ é a linguagem de baixo nível que fala diretamente com o processador. É rápida, eficiente e essencial para o Firmware.

🏗️ Estrutura Básica:
void setup() { ... } 🏁: Executado uma única vez ao ligar. Serve para configurações.

void loop() { ... } 🔄: O ciclo infinito onde a lógica principal acontece.

📝 Exemplo de Código (Blink 💡):
C++
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Configura o LED interno como saída
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Liga o LED
  delay(1000);                     // Espera 1 segundo
  digitalWrite(LED_BUILTIN, LOW);  // Desliga o LED
  delay(1000);                     // Espera 1 segundo
}
3. 🐍 Programação em Python (A Inteligência no Gateway)
Enquanto o C++ cuida do sensor, o Python cuida da inteligência, da rede e do armazenamento na nuvem ou no gateway (como um Raspberry Pi).

🌟 Por que Python na IoT?
📡 Comunicação: Integração fácil via Serial ou Protocolos Web.

📊 Dados: Bibliotecas incríveis para análise (Pandas, Matplotlib).

☁️ Cloud: Conecta seu projeto a APIs e bancos de dados rapidamente.

📝 Exemplo de Leitura de Dados (Python + Serial 📟):
Python
import serial # Biblioteca para falar com o Arduino

# Configura a conexão (Verifique a porta no seu PC!)
conexao = serial.Serial('COM3', 9600)

print("👂 Ouvindo o Arduino...")

while True:
    if conexao.in_waiting > 0:
        dados = conexao.readline().decode('utf-8').strip()
        print(f"📥 Dado recebido: {dados}")
4. 🔗 A Ponte da Arquitetura
Uma solução IoT completa funciona assim:

Sensor 🌡️ -> Detecta mudança no ambiente.

Arduino (C++) 🤖 -> Processa o sinal e envia via Serial/Wi-Fi.

Gateway (Python) 🐍 -> Recebe, filtra e envia para a Nuvem ☁️.

Usuário 📱 -> Visualiza os dados em um Dashboard.