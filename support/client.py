import socket
import threading
import sys
import requests

def receive_data(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received message from server: {data}")
        except socket.error:
            break

def send_data(client_socket):
    while True:
        message = input("Enter a message (Press Enter to stop): ")
        if message == "":
            client_socket.send(b"exit")
            break
        client_socket.send(message.encode())

def connect_to_server(host, port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))

        # Start a separate thread to receive data from the server
        receive_thread = threading.Thread(target=receive_data, args=(client_socket,))
        receive_thread.start()

        # Start a separate thread to send data to the server
        send_thread = threading.Thread(target=send_data, args=(client_socket,))
        send_thread.start()

        # Wait for the send thread to complete
        send_thread.join()

    except socket.error as e:
        print(f"Socket error: {str(e)}")
        sys.exit(1)

    finally:
        # Close the connection
        client_socket.close()
        sys.exit(0)


if __name__ == '__main__':
    
    # host = input("Enter the server's IP address: ")
    host = '127.0.0.1'  # Replace with the server's IP address
    port = input("Enter the server's port: ")

    try:
        # Convert the port to an integer
        port = int(port)
    except ValueError:
        print("Invalid port value. Port must be an integer.")
        sys.exit(1)

    connect_to_server(host, port)
