import socket

def main():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client.connect(('localhost', 5000))  # Replace 'localhost' with the server's IP address if needed
    print("Connected to server")

    # Receive and print welcome message
    welcome_message = client.recv(1024).decode('utf-8')
    print(welcome_message)

    while True:
        # Receive prompt from server
        prompt = client.recv(1024).decode('utf-8')
        print(prompt, end='')

        # Get user input and send to server
        user_input = input()
        client.send(user_input.encode('utf-8'))

        # Receive and print server response
        response = client.recv(1024).decode('utf-8')
        print(response)

        # Check if the server has indicated the end of the game
        if "Summon Complete!" in response:
            break

    # Close the connection
    client.close()

if __name__ == "__main__":
    main()