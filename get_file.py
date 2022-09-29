from datetime import date
import pandas
import requests




def get_file(url):
    response = requests.get(url)
    with open("Daily_checklist.xlsx", "wb") as f:
        f.write(response.content)

