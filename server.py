import socket
import threading
from gacha import GachaGame

# Function to handle client connections
def handle_client(client_socket):
    try:
        # Send a welcome message to the client
        client_socket.send(b"Welcome to the Gacha Game!\n")

        # Main game loop
        while True:
            # Receive the client's choice
            client_socket.send(b"Enter the number of draws you want: ")
            gacha_num = client_socket.recv(1024).decode('utf-8').strip()

            if gacha_num.isdigit():
                gacha_num = int(gacha_num)
                client_socket.send(f"You chose {gacha_num} draws.\n".encode('utf-8'))
                # Perform gacha draws and send results to the client
                for _ in range(gacha_num):
                    result = GachaGame.char_gacha()
                    client_socket.send(f"Gacha result: {result}-Star Item\n".encode('utf-8'))
                client_socket.send(f"✨ Summon Complete! ✨\n")
                break
            else:
                client_socket.send(b"Invalid input. Please enter a valid number.\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client connection
        client_socket.close()

# Function to handle host interactions
def handle_host():
    try:
        print("Welcome to the Gacha Game!\n")

        # Main game loop
        while True:
            # Receive the host's choice
            gacha_num = input("Enter the number of draws you want: ").strip()

            if gacha_num.isdigit():
                gacha_num = int(gacha_num)
                print(f"You chose {gacha_num} draws.")
                # Perform gacha draws and print results
                for _ in range(gacha_num):
                    result = GachaGame.char_gacha()
                    print(f"Gacha result: {result}-Star Item")
                print("✨ Summon Complete! ✨")
                break
            else:
                print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")

# Main server function
def main():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an IP address and port
    server.bind(('0.0.0.0', 5000))

    # Listen for incoming connections
    server.listen(1)  # Only allow one connection at a time
    print("Server listening on port 5000")

    # Accept a new client connection
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")

    # Start a thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    # Handle the host interactions
    handle_host()

    # Wait for the client thread to finish
    client_thread.join()

if __name__ == "__main__":
    main()