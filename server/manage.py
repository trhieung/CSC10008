
from appCtr import AppCtr
from PyQt5 import QtWidgets

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServerWindow = QtWidgets.QMainWindow()

    myApp = AppCtr()
    myApp.setupApp(MainWindow=ServerWindow)
    
    # Connect the aboutToQuit signal to your handle_close function
    app.aboutToQuit.connect(myApp.handle_close)
    
    ServerWindow.show()
    sys.exit(app.exec())