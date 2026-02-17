from socket import * 
import vgamepad as vg

"""
Outcoming packet:
    rumble_large = [0,255]
    rumble_small = [0,255]
    led_num = [0,255]
    RTSP stuff (video and audio)
"""

serverName = "192.168.1.178" 
serverPort = 648 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind((serverName, serverPort)) 
print ("\nThe server is ready to receive\n")  

# Start the DualShock controller
gamepad = vg.VDS4Gamepad()

while 1:
    message, clientAddress = serverSocket.recvfrom(2048) 
    print("Message From Client:" +str(clientAddress)) 
    print("Processing...") 
    modifiedMessage = message.upper() 
    serverSocket.sendto(modifiedMessage, clientAddress) 
    print("Sending a Message to the Client:" +str(clientAddress)) 
