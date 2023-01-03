import socket #importa socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #comunicação cliente e servidor
servidor.bind(('localhost', 8888)) #define endereço do servidor e porta

servidor.listen() #servidor 'escuta' as conexões
client, end = servidor.accept() #aceita as conexões

terminado = False #define terminado para loop

while not terminado: #loop´enquanto o chat não for encerrado, continuará rodando
    msg = client.recv(1024).decode('utf-8') #define a quantidade de bits da mensagem e caracteres
    if msg == 'exit()': #define uma palavra para encerrar o chat
        terminado = True
    else:
        print(msg)
    client.send(input("Mensagem: ").encode('utf-8')) #input da mensagem

client.close() #fecha conexão
servidor.close()#fecha servidor