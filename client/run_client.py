import os 
from socket import *
from Client import Client


# if len(os.argv) < 3: 
#     print("Usage: python client.py <portNumber>") 
#     os.exit() 

# serverIP = os.argv[1]
# serverPort = os.argv[2]

serverName = "localhost" 
serverPort = 5000

try: 
    c = Client(serverName, serverPort) 
except FileNotFoundError: 
    
    sys.exit()

loginSuccess = False
while not loginSuccess:
    username = input("Username: ") 
    password = input("Password: ") 
    loginSuccess =  c.login(username, password) 

c.listen()
