
from appCtr import AppCtr
from PyQt5 import QtWidgets


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServerWindow = QtWidgets.QMainWindow()

    myApp = AppCtr()
    myApp.setupApp(MainWindow=ServerWindow)

    ServerWindow.show()
    sys.exit(app.exec())