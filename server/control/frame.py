
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QResizeEvent
from PyQt5.QtCore import Qt

from control.button import ButtonControl as bc
from control.label import LabelControl as lc
from control.comboBox import ComboBoxControl as cc
from control.radioButton import radioButtonControl as rc
from control.groupBox import GroupBoxControl as gc


class FrameControl(bc, lc, cc, rc, gc):

    def __init__(self) -> None:
        super().__init__()
        self.login_status = False

    def index(self):

        ## frist define the ui
        self.home_func()

        ## active all the control
        self.label_handel()
        self.button_handel()
        self.comboBox_handle()
        self.radioButton_handle()

    def FrameHandel(self) -> None:
        self.index()
