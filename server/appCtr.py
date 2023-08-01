
from control.control import Control
import signal
import os

class AppCtr(Control):

    def __init__(self) -> None:
        super().__init__()

    def setupApp(self, MainWindow):

        self._mainWindow = MainWindow ## this equal to self.centralwidget
        self.setupUi(MainWindow)

        self.FrameHandel() ## initialize in frame.py

        # Connect the resize event of the centralwidget to a slot in control.py
        self.centralwidget.resizeEvent = self.onCentralWidgetResize
    
    def handle_close(self):
        # Your cleanup code or actions before the application exits
        print("Closing the application...")

        if self.sock_thread != None:
            self.sock_thread.join()


        
        


