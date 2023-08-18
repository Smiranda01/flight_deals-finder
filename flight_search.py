import requests
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv()

DEPARTURE_CITY = "SYD"
TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
API_KEY = {"apikey": os.getenv("API_KEY")}


class FlightSearch:
    def __init__(self):
        self.flight_data = {}

    def search_for_code(self, city_name):
        params = {"term": city_name, "location_types": "city"}
        response = requests.get(f"{TEQUILA_ENDPOINT}locations/query", params=params, headers=API_KEY)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def search_for_flight(self, arrival_city, date_from, date_to):
        params = {
            "fly_from": DEPARTURE_CITY,
            "fly_to": arrival_city,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 2,
            "one_for_city": 1,
            "curr": "AUD",

        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}v2/search", params=params, headers=API_KEY)
        try:
            data = response.json()["data"][0]
        except IndexError:
            return f"No flight found for {arrival_city} from {date_from} to {date_to}"
        flight_data = FlightData(
            price=data["price"],
            arrival_airport_code=data["flyTo"],
            arrival_city=data["cityTo"],
            departure_airport_code=data["flyFrom"],
            departure_city=data["cityFrom"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][-1]["local_departure"].split("T")[0],
            stop_over=len(data["route"]) - 2,
            via=data["route"][0]["cityTo"]
        )

        return {
            "price": flight_data.price,
            "arrival_code": flight_data.arrival_airport_code,
            "arrival_city": flight_data.arrival_city,
            "departure_code": flight_data.departure_airport_code,
            "departure_city": flight_data.departure_city,
            "departure_date": flight_data.departure_date,
            "return_date": flight_data.return_date,
            "stop_over": flight_data.stop_over,
            "via": flight_data.via
        }


