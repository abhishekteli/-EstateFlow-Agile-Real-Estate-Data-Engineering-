import requests
import json
import os
import logging
from datetime import date
import time
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()


class Bronze:
    def __init__(self):
        self.basedir = (f"~/Data/rawData/"
                        f"year={date.today().year}/month={date.today().month}/day={date.today().day}/")

    def getRequest(self, loca, home_type, current_page=1):
        try:
            url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
            querystring = {"location": loca, "page": current_page, "home_type": home_type}
            headers = {
                "X-RapidAPI-Key": os.getenv('X-RAPIDAPI-KEY'),
                "X-RapidAPI-Host": os.getenv('X-RAPIDAPI-HOST')
            }
            response = requests.get(url, headers=headers, params=querystring)
            return response
        except requests.exceptions.RequestException as req_err:
            logging.error(f'Request error occurred: {req_err}')

        except ValueError as json_err:
            logging.error(f'JSON decode error: {json_err}')

        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')

    def getTotalPages(self, loca, home_type):
        response = self.getRequest(loca, home_type, 1)
        if response:
            return response.json()['totalPages']
        else:
            return 0

    def extractAndSaveRawData(self, loca, home_type, current_page, total_pages):
        while current_page <= total_pages:
            print(f"Extracting Data for location : {loca} from page no: {current_page}...", end='')
            response = self.getRequest(loca, home_type, 1)
            data = response.json()['props']

            if not os.path.exists(self.basedir):
                os.makedirs(self.basedir)

            with open(f"{self.basedir}/{loca}{current_page}.json", 'w') as file:
                json.dump(data, file)

            print('Done')
            current_page = current_page + 1
            time.sleep(15)


if __name__ == "__main__":
    brnz = Bronze()
    location = ['alpharetta, ga', 'san jose, ca', 'syracuse, ny']#sample places !!! We can add more places
    homeType = 'Apartments_Condos_Co-ops'
    for loc in location:
        totalPages = brnz.getTotalPages(loc, homeType)
        brnz.extractAndSaveRawData(loc, homeType, 1, totalPages)

