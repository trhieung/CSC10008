import os
import json
from utils.data.get_all_data_by_day import get_all_data


class PROCEDURE:
    def __init__(self):
        self.pro_ls = [ {"name": "ls", "args": []},
                        {"name": "get_list_bank", "args": []}, 
                        {"name": "get_newest_bank_data", "args": [str]},
                        {"name": "add_two_num", "args": [int, int]}]
        
    def ls(self) -> str:
        return  str(self.pro_ls)

    def get_list_bank(self, file_path="server/storage/data/banks_url.json") -> str:
        directory = os.path.join(file_path)
        with open(directory, "r") as file:
            data = json.load(file)

        return [item['bank_name'] for item in data]
    
    def get_newest_bank_data(self, bank_name) -> str:
        # Get all data from API
        get_all_data()
        
        if bank_name not in self.get_list_bank():
            return "Invalid bank name"

        #define the path to the bankjson for getting data
        directory = os.path.join(f"server/storage/data/{bank_name}.json")
        with open(directory, "r") as file:
            data = json.load(file)

        return data[0]["data"]
    
    def get_bank_data(self, bank_name, time):
        return []
    
    def add_two_num(self, a, b) -> str:
        try:
            a = float(a)
            b = float(b)
            return a + b
        except ValueError as e:
            raise Exception("Invalid arguments. Both 'a' and 'b' must be numbers.") from e

def test_pro_class():
    pro = PROCEDURE()
    print(pro.get_list_bank())

# test_pro_class()