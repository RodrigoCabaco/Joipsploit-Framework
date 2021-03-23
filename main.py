import colored
from os import system, name

green = colored.fg('green')
red = colored.fg('red')
white = colored.fg('white')
payloads = ['Windows/windows_shell_reverse_tcp','Linux/linux_shell_reverse_tcp']

def clear():
    if name == 'nt': 
        _ = system('cls') 
    
    else: 
        _ = system('clear') 

def showPayloads():
    for payload in payloads:
        print(payload)

def generatePayload(payload, lhost, lport):
    os.system(f'pythonw {payload.split("/")[0]}/generate_{payload.split("/")[1]}')
