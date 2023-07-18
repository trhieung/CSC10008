from  MainWindow import Ui_ServerWindow
from PyQt5.QtGui import QPixmap

class LabelControl(Ui_ServerWindow):
    
    def __init__(self) -> None:
        super().__init__()

    def background_func(self):
        # Load image
        self.pixmap = QPixmap('server/storage/background.jpg')

        # Set pixmap to the label
        self.label_background.setPixmap(self.pixmap)


    def label_handel(self):
        pass
        # self.background_func()