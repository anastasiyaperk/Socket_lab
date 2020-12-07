import socket
import sqlite3 as sl3

dbconn = sl3.connect('messages.db')
cursor = dbconn.cursor()

soc = socket.socket()
soc.bind(("", 13000))
soc.listen(1)
print('Waiting for connection...')
while True:
    conn, addr = soc.accept()
    receivedData = conn.recv(1024)
    decodedString = receivedData.decode('utf-8')

    if decodedString == "LIST":
        messages = []
        selectQuery = "SELECT message from messages"
        with dbconn:
            cursor.execute(selectQuery)
        listOfMessages = cursor.fetchall()
        for row in listOfMessages:
            messages.append(row[0])
        for message in messages:
            print(message)
            conn.send(message.encode('utf-8'))
    else:
        insertQuery = "INSERT INTO messages (id, message) values (null, ?)"
        data = (decodedString,)
        with dbconn:
            cursor.execute(insertQuery, data)
            infoMessage = 'Message \''+decodedString+'\' added.'
            conn.send(infoMessage.encode('utf-8'))

    conn.close()