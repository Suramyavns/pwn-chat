## Simple Terminal Chat App
### Using Python

This python script can be used to anonymously chat to a remote IP address. 
The target would initialise a netcat listener on local machine.
The host would then establish a connection to the target's IP and port through this script.

Note: Use VPN for optimum security.

# Setup: 
1. Clone the repo
2. `cd pwn-chat`
3. `pip install -r requirements.txt`

# Chat:
1. Target: `nc -lvp <port>`
2. Host: `python pwn-chat.py <args>`

NOTE: Run `python pwn-chat.py -h` for help.
