from control.frame import FrameControl

from PyQt5 import QtCore, QtGui, QtWidgets

class Control(FrameControl):

    def __init__(self) -> None:
        super().__init__()

    def onCentralWidgetResize(self, event):
        # # Adjust the size of the frame_index to match the new size of the centralwidget
        # self.frame_index.setGeometry(QtCore.QRect(0, 0, self.centralwidget.width(), self.centralwidget.height()))
        # self.label_background.setGeometry(QtCore.QRect(0, 0, self.centralwidget.width(), self.centralwidget.height()))
        pass


