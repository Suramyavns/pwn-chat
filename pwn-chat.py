import pwn
import socket
import argparse
import termcolor
parser = argparse.ArgumentParser()
parser.add_argument("IP",help="Target IP address",type=str)
parser.add_argument("-p","--port",default=9000,help="Listener port on target",type=int)
args = parser.parse_args()

def chatting(conn,remote,port):
    print(termcolor.colored(f"[+] Connected to {remote}:{port}","green",attrs=['bold']))
    while True:
        msg = input('You: ')
        if msg in ['bye','exit','close']:
            conn.sendline(b'[*] Connection closed by Anonymous')
            break
        line = 'Anonymous: '+msg+'\nYou: '
        lineB = line.encode()
        conn.sendline(lineB)
        print(termcolor.colored('[+] Waiting for reply...','cyan'))
        try:
            print(f'{remote}: {conn.recvline().decode()}')
        except EOFError:
            print(termcolor.colored(f'[*] Connection closed by {remote}','yellow',attrs=['bold']))
            break
        conn.sendline(b'[+] Waiting for reply...')
    conn.close()


def getValidIP(remote):
    try:
        socket.inet_aton(remote)
        return remote
    except socket.error:
        return False

def getValidPort(port):
    if int(port)>=0 and int(port)<=65535:
        return port
    else:
        return True
if args.IP and args.port:
    remote = args.IP
    port = args.port
    if(getValidIP(remote)):
        if(getValidPort(port)):
            try:
                conn = pwn.remote(remote,port=port)
                chatting(conn,remote,port)
            except:
                print(termcolor.colored("[-] Target is down.",'light_red',attrs=['bold']))
        else:
            print(termcolor.colored('[!] Invalid port number','light_red',attrs=['bold']))
    else:
        print(termcolor.colored("[!] Invalid IP address",'light_red',attrs=['bold']))