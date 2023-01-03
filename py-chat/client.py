import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #comunicação cliente e servidor

client.connect(('localhost', 8888))   #define endereço do servidor e porta

terminado = False   #define terminado para loop

print('digite exit() para terminar o chat')


while not terminado:
    client.send(input("Mensagem: ").encode('utf-8')) #input da mensagem
    msg = client.recv(1024).decode('utf-8')  #define a quantidade de bits da mensagem e caracteres
    if msg == 'exit()':  #define uma palavra para encerrar o chat
        terminado = True
    else:
        print(msg)
client.close() #fecha conexão