#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# APIs used in this project
# Sheety to write to a Google Sheet
# Tequila Kiwi to get flight data
# Twilio to send SMSes

useful

from pprint import pprint
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

KIWI_API_KEY = os.getenv('KIWI_API_KEY')
NUT_URL = f"{NUT_DOMAIN}{NUT_ENDPOINT}"
SHEETY_URL = os.getenv('SHEETY_API_URL')
SHEETY_BEARER_TOKEN = os.getenv('SHEETY_BEARER_TOKEN')

# Continue from 339
# do not forget to push the workout tracker and also this project to GitHub
