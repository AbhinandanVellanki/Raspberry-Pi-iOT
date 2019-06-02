import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect the socket to the port where the server is listening
# 'localhost' means this computer
# 12345 is the port number
server_address = ('localhost', 12345)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

    
# Send data
# character string is encoded using "utf-8" before sending
message = "I am attending ELEC2840."
print('sending "%s"' % message)
sock.send(message.encode("utf-8"))


# read the reply from server
# data is decoded before printing out as string
data = sock.recv(1024)
print('received "%s"' % data.decode("utf-8"))


# close the connection
print('closing socket')
sock.close()

