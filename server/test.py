from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ComboBox Example')

        # Create a QVBoxLayout to hold the combo box
        layout = QVBoxLayout()

        # Create the combo box
        combo_box = QComboBox()
        
        # Add bank names to the combo box
        bank_names = ['Bank A', 'Bank B', 'Bank C', 'Bank D']
        combo_box.addItems(bank_names)

        # Add the combo box to the layout
        layout.addWidget(combo_box)

        # Set the layout for the main window
        self.setLayout(layout)
