from socket import * 

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
"""

serverName = gethostname() 
serverPort = 648

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("\nInput lowercase sentence:")
clientSocket.sendto(message.encode(), (serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print("\nMessage Sent to Server :" +str(serverAddress))
print("Receiving Message From the Server...") 
print("Your Sentence :"+ modifiedMessage.decode()) 
clientSocket.close()
