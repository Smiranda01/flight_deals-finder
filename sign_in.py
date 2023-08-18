import requests
from dotenv import load_dotenv
import os

load_dotenv()

ENDPOINT = os.getenv("USERS_SHEETY_ENDPOINT")
HEADERS = {"Authorization": os.getenv("AUTH")}


class Signer:

    def __init__(self):
        self.email_coincides = False
        self.email = ""

    def ask_for_details(self):
        print("Welcome to Santiago's Flight Club")
        print("We find the best flight deals and email you")
        name = input("What's your fist name?\n")
        last_name = input("What's is your last name?\n")
        while not self.email_coincides:
            self.email = input("What's your email?\n")
            print(f"You typed {self.email}")
            confirm_email = input("Type your email again\n")
            if self.email != confirm_email:
                print("Email has to match!")
            elif self.email == confirm_email:
                print("Welcome you're part of the club")
                self.email_coincides = True

        self.upload_details(name, last_name, self.email)

    def upload_details(self, first_name, last_name, email):
        params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email

            }
        }
        response = requests.post(url=ENDPOINT, json=params, headers=HEADERS)
        print(response.text)
        print(response.raise_for_status())
