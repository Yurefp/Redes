import socket
import threading
import os

HEADER = 64
PORT = 18000
FORMAT = "utf-8"
DISCONNECT_MESAGE = "!DISCONNECT"
SERVER = "10.10.11.10"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def enviar(texto):
    txt = texto.encode(FORMAT)
    txt_len = str(len(txt)).encode(FORMAT)
    txt_len += b' ' * (HEADER - len(txt_len))
    client.send(txt_len)
    client.send(txt)
    print(client.recv(2048).decode(FORMAT))

while True:
    mensagem = input("Mensagem:")
    enviar(mensagem)