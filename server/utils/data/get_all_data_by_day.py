import requests
import json
import os
import datetime

def save_data_to_json(data, file_path):
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist

    with open(file_path, "w") as file:
        json.dump(data, file)

def get_banks_url(file_path):
    directory = os.path.dirname(file_path)


    with open(file_path, "r") as file:
        data = json.load(file)
        return [{'bank_name': item['bank_name'], 'url': item['url_exchange_rate_get']} for item in data]


def get_all_data():
    # Get api key
    response = requests.get('https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate')
    api_key = response.json()["results"]
    # print(api_key)

    # define bank_url
    banks_url = get_banks_url('server/storage/data/banks_url.json')
    # each_url = {"bank_name": "SBV", "url": "https://vapi.vnappmob.com/api/v2/exchange_rate/sbv"}

    # Set up the request headers with the API key
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # Send a GET request to the API endpoint
    for bank_url in banks_url:
        bank_name = bank_url["bank_name"]
        response = requests.get(bank_url["url"], headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            try:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = response.json()
                bank = [{"data": data["results"], "time": current_time}]

                save_data_to_json(bank, file_path=f"server/storage/data/{bank_name}.json")
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON response from {bank_name} API, {str(e)}")
        else:
            print(f"Error occurred while retrieving data from {bank_name}: {response.status_code}")
