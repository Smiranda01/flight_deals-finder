# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
from sign_in import Signer

sign_in = Signer()
flight_search = FlightSearch()
data = DataManager()
sheety_data = data.get_sheet_data()
sign_user = input("Do you wanna sign a user in? Type Yes/No\n").lower()

if sign_user == "yes":
    sign_in.ask_for_details()

if sheety_data[0]["iataCode"] == "":
    for city in sheety_data:
        city["iataCode"] = flight_search.search_for_code(city["city"])
    print(sheety_data)

    data.sheet_data = sheety_data
    data.update_code()
print(sheety_data)

now = datetime.now()
tomorrow = now + timedelta(days=1)
six_months = now + timedelta(days=(6 * 30))

for city in sheety_data:
    flight_found = flight_search.search_for_flight(arrival_city=city["iataCode"], date_from=tomorrow,
                                                   date_to=six_months)
    try:
        if int(flight_found["price"]) < int(city["lowestPrice"]):
            print("Loading...")
    except TypeError:
        print(flight_found)
    else:
        print(f"Flight found for {flight_found['arrival_city']}")
        notification_manager = NotificationManager()
        notification_manager.send_email_to_customers(flight_found)

