import socket
HOST = "localhost" # Aonde o servidor está, IP, etc.
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST,PORT)) # Quer dizer que o servidor estabeleceu em um determinado ip e porta, o client não precisa estabelecer e sim conectar

sock.listen(5)

while True:
    novoSock, _ = sock.accept()
    nomeArquivo = novoSock.recv(1024).decode() #Receber uma mensagem e agora vai decodificar
    novoArquivo = novoSock.recv(100000)
    
    with open(f"Arquivos/{nomeArquivo}.png", "wb") as arq:
        arq.write(novoArquivo)
 
    novoSock.send(b"ok")

'''     mensagem = novoSock.recv(1024) #Receber uma mensagem e por ser indo pela rede é sempre em binario
        print(mensagem)
        novoSock.send(b"ok")'''