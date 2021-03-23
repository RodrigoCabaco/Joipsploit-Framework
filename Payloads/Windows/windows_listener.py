import socket
import threading
import os
import sys

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.bind((HOST,PORT))
listener.listen()
print(f'Started Listener on {HOST}:{PORT}')
clients = []

def receiveMessage(client):
    while True:
        message = client.recv(2048).decode('ascii')
        print("\n"+message)

def sendMessage():
    while True:
        try:
            for client in clients:
                print(f"=> ",end='')
                client.send(input().encode('ascii'))
        except:
            print("Error sending command")

def getSignal():
    while True:
        client, address = listener.accept()
        print("New connection: " + str(address))
        clients.append(client)
        thread = threading.Thread(target=receiveMessage,args=(client,))
        thread2 = threading.Thread(target=sendMessage)
        thread.start()
        thread2.start()

getSignal() 
