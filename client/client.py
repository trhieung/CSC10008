import socket
import json

class ClientSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print("Connected to server")

    def send_request(self, request):
        self.client_socket.sendall(request.encode())

        response = self.client_socket.recv(1024).decode()
        print("Response:", response)

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    # Replace these values with the server's IP address and port
    host = '127.0.0.1'
    port = 12345

    client_socket = ClientSocket(host, port)
    client_socket.connect()

    while True:
        try:
            request_name = input("Enter procedure name: ")
            request_args = input("Enter procedure arguments (comma-separated): ")
            if not request_args:
                request_args = []
            else:
                request_args = [arg.strip() for arg in request_args.split(",")]

            request_data = {"name": request_name, "args": request_args}
            request_message = json.dumps(request_data)

            client_socket.send_request(request_message)

        except KeyboardInterrupt:
            print("\nClient closed.")
            break

        except Exception as e:
            print("Error:", e)

    client_socket.close()
