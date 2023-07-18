from  MainWindow import Ui_ServerWindow
from control.groupBox import GroupBoxControl as gc
import os
import json
# from control.comboBox import ComboBoxControl as cc

class radioButtonControl(Ui_ServerWindow):
    
    def __init__(self):
        super().__init__()

    def update_status(self) -> None:
        bank_name = self.comboBox_banks.currentText()

        directory = os.path.join(f'server/storage/data/{bank_name}.json')

        with open(directory, "r") as file:
            json_data = json.load(file)

        gc.plot(self, data_index_plot=json_data[0])

    def radioButton_handle(self) -> None:
        self.radioButton_table.clicked.connect(lambda: self.update_status())
        self.radioButton_chart.clicked.connect(lambda: self.update_status())


