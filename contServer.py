from socket import * 
import vgamepad as vg

"""
Incoming packet:
    pressed = 0b0000010000010000 # Right trigger and square pressing
    specials = 0b01 # PS button pressing
    dpad = 0b0000
    l3x = 0.0
    l3y = 1.0
    r3x = 0.0
    r3y = 0.0
    # After this, this variables are optional
    rt = 0x0
    lt = 0x255
    touchx: U16 = 0x861
    touchy: U16 = 0x500
    acx, acy, acz: U16 # Accelerometer
    gyx, gyy, gyz: U16 # Gyroscope
    microphone:PackedBytes # maybe??????

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
