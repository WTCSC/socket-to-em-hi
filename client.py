import socket

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to 0.0.0.0:5000
server.bind(('0.0.0.0', 5000))

# Listen for connections
server.listen(1)
print("Waiting for connection...")

# Accept client connection
client, addr = server.accept()
print(f"Connected to {addr}")

client.close()
server.close()