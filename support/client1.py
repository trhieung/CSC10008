import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.terminate_flag = threading.Event()

    def listen_server_termination(self):
        while not self.terminate_flag.is_set():
            try:
                data = self.server_socket.recv(1024).decode()
                if data.lower() == "exit":
                    print("Received termination signal from the server. Terminating...")
                    self.terminate_flag.set()
            except ConnectionAbortedError:
                break
        self.server_socket.close()

    def send_and_receive_data(self):
        while not self.terminate_flag.is_set():
            message = input("Enter a message to send (press enter to terminate): ")
            if message.lower() == "":
                self.server_socket.send(message.encode())
                self.terminate_flag.set()
                break

            self.server_socket.send(message.encode())
            response = self.server_socket.recv(1024).decode()
            print(f"Server response: {response}")

        self.server_socket.close()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((self.host, self.port))

        termination_thread = threading.Thread(target=self.listen_server_termination)
        data_thread = threading.Thread(target=self.send_and_receive_data)

        termination_thread.start()
        data_thread.start()

        termination_thread.join()
        data_thread.join()

if __name__ == "__main__":
    host = '127.0.0.1'  # Replace with the server's IP address
    port = 12345        # Replace with the server's port
    client = Client(host, port)
    client.start()
