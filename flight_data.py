DEPARTURE_CITY = "Sydney"


class FlightData:

    def __init__(self, price, departure_airport_code, arrival_airport_code, departure_city, arrival_city, departure_date
                 , return_date, stop_over, via):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.arrival_airport_code = arrival_airport_code
        self.arrival_city = arrival_city
        self.departure_date = departure_date
        self.return_date = return_date
        self.stop_over = stop_over
        self.via = via
