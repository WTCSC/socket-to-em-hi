import socket

def main():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    ip_address = input("Enter the server's IP address: ")
    port = int(input("Enter the server's port number: "))

    try:
        client.connect((ip_address, port))
        print("Connected to server")

        # Receive and print welcome message
        welcome_message = client.recv(1024).decode('utf-8')
        print(welcome_message)

        while True:
            # Receive prompt from server
            prompt = client.recv(1024).decode('utf-8')
            if not prompt:  
                print("Server closed the connection.")
                break  
            print(prompt, end='')

            # Get user input and send to server
            user_input = input().strip()
            if not user_input:  
                print("Please enter a valid input.")
                continue  

            client.send(user_input.encode('utf-8'))

            # Receive and print server response
            response = client.recv(1024).decode('utf-8')
            if not response:  
                print("Server disconnected.")
                break  
            print(response)

            if "Exit" in response:
                break  
                
    except ConnectionResetError:
        print("Connection lost. Server may have crashed or closed.")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client.close()
        print("Connection closed")

if __name__ == "__main__":
    main()