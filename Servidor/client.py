import socket
HOST = "localhost" # Aonde o servidor está, IP, etc.
PORT = 8002

filename = input(f"Nome do arquivo e extensão: ")

arquivo = open(f'{filename}', "rb")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST,PORT))

#sock.send("teste") # não da certo pois é uma string
#sock.send(b"teste") # Agora está no fomato de byte

sock.send(input("Digite qual será o nome do arquivo: ").encode()) # Vai transformar o input em binario

sock.send(arquivo.read())
confirmacao = sock.recv(1024)
if confirmacao == b"ok":
    print("Mensagem recebida")