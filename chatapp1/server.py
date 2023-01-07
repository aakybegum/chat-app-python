from socket import *
from threading import *

server = socket(AF_INET, SOCK_STREAM)

HOST = '192.168.1.108'
PORT = 5038
server.bind((HOST, PORT))
server.listen()
print('Server açık.')

clients = []
names = []


def clientThread(client):
    x = True
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if x:
                names.append(message)
                print(message, ' bağlandı')
                x = False
            for c in clients:
                if c != client:
                    index = clients.index(client)
                    name = names[index]
                    index = clients.index(client)
                    if index < len(names):
                        name = names[index]
                    else:
                        index = index % len(names)
                        name = names[index]

                    c.send((name + ':' + message).encode('utf8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            name = names[index]
            names.remove(name)
            print(name + ' çıktı')
            break

while True:
    client, address = server.accept()
    clients.append(client)
    print('Bağlantı yapıldı.', address[0] + ':' + str(address[1]))
    thread = Thread(target=clientThread, args=(client,))
    thread.start()
