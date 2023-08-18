import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_ENDPOINT = os.getenv("FLIGHT_SHEETY_ENDPOINT")
HEADERS = {"Authorization": os.getenv("AUTH")}
print(type(HEADERS))

class DataManager:

    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
        self.sheet_data = response.json()
        print(response.text)
        return self.sheet_data["prices"]

    def update_code(self):
        print(self.sheet_data)
        for city in self.sheet_data:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=parameters, headers=HEADERS)
            print(response.text)
