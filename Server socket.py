import socket
#importa a bib socket

SERVER_IP = ''
# Endereco IP do Servidor, '' = significa que ouvira em todas as interfaces

LISTEN_PORT =6000
# Porta que o Servidor vai ouvir

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.SOCK_DGRAM=usaremos UDP

SERVER_CONN = (SERVER_IP, LISTEN_PORT)
udp.bind(SERVER_CONN)
# faz o bind do ip e a porta para que possa comecar a ouvir

#Mensagem_Recebida, END_cliente = udp.recvfrom(1024)
#socket.recvfrom(bufsize[, flags])  deve ser uma potencia de 2


with udp:
    print("conected by Server String OCEANICASUB VII")
    while True:
        data = udp.recv(10240)
        print (data)
        if not data:
            continue


udp.close()