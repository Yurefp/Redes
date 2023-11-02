import socket
import threading

HEADER = 64                         #Define o tamanho do cabeçalho
PORT = 18000                        #Define a porta que o cliente irá enviar as mensagens para o servidor
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = ""
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def enviar(texto):
    txt = texto.encode(FORMAT)
    txt_len = str(len(txt)).encode(FORMAT)
    txt_len += b' ' * (HEADER - len(txt_len))
    client.send(txt_len)
    client.send(txt)

def receber_mensagens():
    while True:
        message = client.recv(2048).decode(FORMAT)
        if not message:
            mensagem = input("")
            enviar(mensagem)
            break
        print(message)

# Inicie uma thread para receber mensagens do servidor em paralelo
receber_thread = threading.Thread(target=receber_mensagens)
receber_thread.start()

while True:
    mensagem = input("")
    enviar(mensagem)

# Quando você quiser desconectar, envie a mensagem de desconexão
enviar(DISCONNECT_MESSAGE)