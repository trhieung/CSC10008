from  MainWindow import Ui_ServerWindow
import os
import json

class ComboBoxControl(Ui_ServerWindow):
    
    def __init__(self):
        super().__init__()

    def banks(self) -> None:
        def get_banks_name(file_path = 'server/storage/data/banks_url.json'):
            directory = os.path.join(file_path)

            with open(directory, "r") as file:
                data = json.load(file)
                return [item['bank_name'] for item in data]

        def handle_selection(index):
            pass
            # print(self.comboBox_banks.currentText())

        ##
        self.comboBox_banks.addItems(get_banks_name())
        self.comboBox_banks.currentIndexChanged.connect(handle_selection)

    def money_types(self) -> None:
        def get_types(self) -> list:
            bank_name = self.comboBox_banks.currentText()
            directory = os.path.join(f'server/storage/data/{bank_name}.json')

            with open(directory, "r") as file:
                json_data = json.load(file)

            return list(json_data[0]['data'][0].keys())
        
        keys = get_types(self)
        keys.remove("currency")
        self.comboBox_money_type.clear()
        self.comboBox_money_type.addItems(keys)

    def comboBox_handle(self) -> None:
        self.banks()
        self.money_types()

        self.comboBox_banks.currentTextChanged.connect(self.money_types)
