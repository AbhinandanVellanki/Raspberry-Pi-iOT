import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
# 12345 is the port number
server_address = ('', 12345)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# a server keeps running forever
while True:

    # Wait for a connection
    print('waiting for a connection')

    # accept an incoming connection
    connection, client_address = sock.accept()
    print('connection from', client_address)

    # receive data and send it back
    data = connection.recv(1024)
    print('received "%s"' % data.decode("utf-8"))
    connection.send(data)

    # close this connection 
    connection.close()
    print("connection closed\n")
