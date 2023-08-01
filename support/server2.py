import socket
import threading
import json

class PROCEDURE:
    def __init__(self):
        self.pro_ls = [ {"name": "get_list_bank", "args": []}, 
                        {"name": "get_newest_bank_data", "args": []},
                        {"name": "add_two_num", "args": [int, int]}]

    def get_list_bank(self) -> str:
        return ["a", "b"]
    
    def get_newest_bank_data(self) -> str:
        return [{"doanxe": 12}, {"doanxem": 13}]
    
    def add_two_num(self, a, b) -> str:
        try:
            a = float(a)
            b = float(b)
            return a + b
        except ValueError as e:
            raise Exception("Invalid arguments. Both 'a' and 'b' must be numbers.") from e
    
class ServerSocket:
    def __init__(self):
        self.terminate_flag = None
        self.server_socket = None

        # List to hold active client connections
        self.client_threads = []
        self.term_thread = None

        # initial procedure in order to access db
        self.procedure = PROCEDURE()

    def termination_thread(self):
        input("Press Enter to stop the server.\n")

        # handle something else if you want after shutdown the server
        try:
            pass
        except:
            pass

        # turn on terminate flag
        self.terminate_flag.set()

        # Close all client connections and join sub threads into main thread
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

    def get_response(self, request) -> str:
        # Process the data based on the procedure class
        try:
            request_data = json.loads(request)
            procedure_name = request_data.get("name")
            procedure_args = request_data.get("args", [])

            # Find the procedure by name
            procedure = None
            for proc in self.procedure.pro_ls:
                if proc["name"] == procedure_name:
                    procedure = proc
                    break

            if procedure is None:
                raise Exception(f"Procedure '{procedure_name}' not found in the list")

            # Validate the number of arguments
            if len(procedure["args"]) != len(procedure_args):
                raise Exception(f"Invalid number of arguments for procedure '{procedure_name}'")

            # Call the procedure with the provided arguments
            if procedure_args:
                result = getattr(self.procedure, procedure_name)(*procedure_args)
            else:
                result = getattr(self.procedure, procedure_name)()

            return json.dumps(result)

        except Exception as e:
            return json.dumps({"error": str(e)})

    def handel_client(self, client_socket, client_address):
        try:
            # Receive request from the client
            while True:
                c_request = client_socket.recv(1024).decode()
                print(f"Received request from client {client_address[0]}:{client_address[1]}: {c_request}")

                if not c_request:
                    break

                # get then send back the response of the request
                response = self.get_response(c_request)
                client_socket.send(response.encode())

        except ConnectionAbortedError:
            print(f"Connection with client {client_address[0]}:{client_address[1]} aborted")

        finally:
            # Close the connection
            client_socket.close()
            print(f"Connection with client {client_address[0]}:{client_address[1]} closed")

            # Remove the terminated thread from self.client_threads
            self.client_threads = [(c_socket, c_address, c_thread) for c_socket, c_address, c_thread in self.client_threads if c_socket != client_socket]


    def start_server(self, host, port):
        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the sicket to a specific address and port
        self.server_socket.bind((host, port))

        # Listen for incoming connections limite = 5 connections
        self.server_socket.listen(5)
        print(f"Server is listening on {host}:{port}")

        # Terminate flag
        self.terminate_flag = threading.Event()

        # Start terminate thread
        self.term_thread = threading.Thread(target=self.termination_thread)
        self.term_thread.start()

        while not self.terminate_flag.set():
            try:
                # Accept a client connection
                client_socket, client_address = self.server_socket.accept()
                print(f"Connected to client: {client_address[0]}:{client_address[1]}")

                # Create new thread to handle the client
                client_thread = threading.Thread(target=self.handel_client, args=(client_socket, client_address))
                client_thread.start()
                
                # Add client thread to the list 
                self.client_threads.append((client_socket, client_address, client_thread))

            except OSError as e:
                if self.terminate_flag.is_set():
                    break
                else:
                    print(f"Error accepting client connection: {str(e)}")
                    continue

        # after terminate flag is set -> turn of ther server, join terminate thread and print message
        self.term_thread.join()
        print("Server stopped")    


    def server_main(self):
        host = '127.0.0.1'  # Replace with your desired IP address
        port = 12345  # Replace with your desired port
        self.start_server(host, port)

if __name__ == "__main__":
    server = ServerSocket()
    server.server_main()
