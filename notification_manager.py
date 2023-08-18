import smtplib
import requests
from dotenv import load_dotenv
import os

load_dotenv()

ENDPOINT = os.getenv("USERS_SHEETY_ENDPOINT")
HEADERS = {"Authorization": os.getenv("AUTH")}
my_gmail = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


class NotificationManager:

    def send_email_to_customers(self, flight_found):
        response = requests.get(url=ENDPOINT, headers=HEADERS)
        data = response.json()["users"]

        for user in data:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=password)
                message = f"Subject:{user['firstName']}, We have a great deal for you!\n\n" \
                          f"Flight details✈️✈️✈️:\n" \
                          f"From {flight_found['departure_city']}/{flight_found['departure_code']}," \
                          f" To {flight_found['arrival_city']}/{flight_found['arrival_code']}" \
                          f" for $AUD{flight_found['price']}\n" \
                          f"Departs on {flight_found['departure_date']} and" \
                          f" Returns {flight_found['return_date']}"
                link = "https://www.google.com/flights"
                if flight_found["stop_over"] > 1:
                    message += f"\nFlight has {flight_found['stop_over']} stop overs, via {flight_found['via']}."
                elif flight_found["stop_over"] > 0:
                    message += f"\nFlight has {flight_found['stop_over']} stop over, via {flight_found['via']}."
                full_message = f"{message}\n\n{link}"
                connection.sendmail(from_addr=my_gmail,
                                    to_addrs=user['email'],
                                    msg=full_message.encode("utf-8"))

# test = NotificationManager()
# test.send_email_to_customers()

# def send_notification(self, flight_found):
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body=f"Flight details✈️✈️✈️:\n"
#            f"From {flight_found['departure_city']}/{flight_found['departure_code']},"
#            f" To {flight_found['arrival_city']}/{flight_found['arrival_code']} for $AUD{flight_found['price']}\n"
#            f"Departs on {flight_found['departure_date']} and Returns {flight_found['return_date']}",
#         from_='+15675871218',
#         to=''
#     )
#     print(message.status)
