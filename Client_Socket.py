import socket


IP_SERVIDOR = '10.7.0.27'

PORTA_Servidor = 5000

print("Escreva a Mensagem a ser enviada:")
Message = str.encode(input())
def sokk():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Message = str.encode(input())


DESTINO = (IP_SERVIDOR, PORTA_Servidor)

with sokk:
    sokk()
    udp.sendto(data, DESTINO)
    if not data:
        udp.close()




    
