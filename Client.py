import socket

print('Hello!\n')

while True:
    soc = socket.socket()
    soc.connect(('localhost', 13000))

    sentString = input("Please, write your message to list:\n")
    sentString = sentString.encode('utf-8')

    soc.send(sentString)
    dataReceived = soc.recv(1024)

    while dataReceived != b'':
        decodedData = dataReceived.decode('utf-8')
        print(decodedData+';')
        dataReceived = soc.recv(1024)

    soc.close()