from socket import * 

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
