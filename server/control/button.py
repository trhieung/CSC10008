from  MainWindow import Ui_ServerWindow
import pymongo
import os
import sys
import threading

# Get the path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path of os.pth by joining it with the current directory
os_path_file = os.path.join(current_dir, "server")

# Check if the os.pth file exists
if os.path.exists(os_path_file):
    # Read the content of os.pth and add each directory to sys.path
    with open(os_path_file, "r") as file:
        for line in file:
            path = line.strip()
            if path not in sys.path:
                sys.path.append(path)

from server import server_main

class ButtonControl(Ui_ServerWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.sock_thread = None
    
    def hide_all_frame(self) -> None:
        self.frame_about.hide()
        self.frame_home.hide()
        self.frame_login.hide()

    def home_func(self) -> None:
        self.hide_all_frame()
        self.frame_home.show()
        self.frame_home.raise_()

    def about_func(self) -> None:
        self.hide_all_frame()
        self.frame_about.show()
        self.frame_about.raise_()

    def contact_func(self) ->None:
        pass

    def login_func(self) -> None:
        # self.frame_home.hide()
        self.frame_login.show()
        self.frame_login.raise_()
    
    def login_close_func(self) -> None:
        self.frame_login.hide()

    def login_submit_func(self) -> None:

        def mongodb_conn(conn_str: str):
            try:
                conn = pymongo.MongoClient(conn_str)
            except pymongo.errors.ConnectionFailure as e:
                print("Could not connect to server: %s", e)

            return conn
        
        def get_hosts(conn_str: str):
            conn = mongodb_conn(conn_str)
            if conn is None:
                # no connection, exit early
                return

            try:
                self.frame_login.hide()
                self.frame_about.raise_()
                self.sock_thread = threading.Thread(target=server_main)
                self.sock_thread.daemon = True
                self.sock_thread.start()
            except:
                print("No hosts found")

        ###
        # mongodb+srv://<username>:<password>@csc10008.tipkf6n.mongodb.net/
        ###
        
        username = self.lineEdit_user.text()
        pwd = self.lineEdit_pwd.text()
        
        connect_str = f"mongodb+srv://{username}:{pwd}@csc10008.tipkf6n.mongodb.net/" # create string to connect to mongdb
        get_hosts(connect_str)

    def button_handel(self):
        self.button_home.clicked.connect(self.home_func)
        self.button_about.clicked.connect(self.about_func)

        self.button_login.clicked.connect(self.login_func)
        self.button_login_close.clicked.connect(self.login_close_func)

        self.button_login_submit.clicked.connect(self.login_submit_func)