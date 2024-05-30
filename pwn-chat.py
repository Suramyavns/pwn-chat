import pwn
import socket

def getValidIP():
    while True:
        remote = input("RHOST: ")
        try:
            socket.inet_aton(remote)
            return remote
            # legal
        except socket.error:
            # Not legal
            print('Invalid IP address')

def getValidPort():
    while True:
        port = input("RPORT: ")
        try:
            if int(port)>=0 and int(port)<=65535:
                return port
            else:
                print('Invalid port number')
        except:
            continue

remote = getValidIP()
port = getValidPort()

conn = pwn.remote(remote,port=port)

while True:
    msg = input('You: ')
    if msg in ['bye','exit','close']:
        conn.sendline(b'Connection closed by Anonymous')
        break
    line = 'Anonymous: '+msg+'\nYou: '
    lineB = line.encode()
    conn.sendline(lineB)
    print('Waiting for reply...')
    try:
        print(f'{remote}: {conn.recvline().decode()}')
    except EOFError:
        print(f'Connection closed by {remote}')
        break
    conn.sendline(b'Waiting for reply...')
conn.close()