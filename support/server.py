import socket
import threading

class server_socket():
    def __init__(self):
        self.terminate_flag = None
        self.server_socket = None

        # List to hold active client connections
        self.client_threads = []

    def handle_client(self, client_socket, client_address):
        try:
            # Receive data from the client
            while True:
                data = client_socket.recv(1024).decode()
                print(f"Received data from client {client_address[0]}:{client_address[1]}: {data}")

                if not data:
                    break

                if data.lower() == "exit":
                    print(f"Client {client_address[0]}:{client_address[1]} requested to exit.")
                    break

                # Process the received data
                response = self.process_data(data)

                # Send a response back to the client
                client_socket.send(response.encode())

        except ConnectionAbortedError:
            print(f"Connection with client {client_address[0]}:{client_address[1]} aborted.")

        finally:
            # Close the connection
            client_socket.close()
            print(f"Connection with client {client_address[0]}:{client_address[1]} closed")

            # Remove the terminated thread from self.client_threads
            self.client_threads = [(c_socket, c_address, c_thread) for c_socket, c_address, c_thread in self.client_threads if c_socket != client_socket]

    def process_data(self, data):
        # Process the data as per the server's requirements
        # Customize this function based on your specific needs
        # Here, we simply echo the received data
        return f"Hello from the server! You sent: {data}"

    def termination_thread(self):
        input("Press Enter to stop the server.\n")

        # Send termination message to all connected clients
        termination_message = "Server is terminating. Goodbye!"
        for client_thread in self.client_threads:
            client_socket, _ = client_thread[:2]
            try:
                client_socket.send(termination_message.encode())
            except OSError as e:
                print(f"Error sending termination message to client: {str(e)}")

        # turn on terminate flag
        self.terminate_flag.set()

        # Close all client connections and join threads
        for client_thread in self.client_threads:
            client_socket, _, thread = client_thread
            try:
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
            except OSError as e:
                print(f"Error closing client socket: {str(e)}")
            thread.join()

        # Close the server socket
        if self.server_socket is not None:
            self.server_socket.close()

    def start_server(self, host, port):
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to a specific address and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(5)
        print(f"Server is listening on {host}:{port}")

        # Termination flag
        self.terminate_flag = threading.Event()

        # Start termination thread
        term_thread = threading.Thread(target=self.termination_thread)
        term_thread.start()

        while not self.terminate_flag.is_set():
            try:
                # Accept a client connection
                client_socket, client_address = server_socket.accept()
                print(f"Connected to client: {client_address[0]}:{client_address[1]}")

                # Create a new thread to handle the client
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()

                # Add client thread to the list
                self.client_threads.append((client_socket, client_address, client_thread))

            except OSError as e:
                if self.terminate_flag.is_set():
                    break
                else:
                    print(f"Error accepting client connection: {str(e)}")
                    continue

        print("Server stopped.")

    def server_main(self):
        host = '127.0.0.1'  # Replace with your desired IP address
        port = 12345  # Replace with your desired port
        self.start_server(host, port)

server = server_socket()
server.server_main()