from datetime import date
import pandas
import requests




def get_file(url):
    response = requests.get(url)
    with open("Daily_checklist.xlsx", "wb") as f:
        f.write(response.content)


# get_file(
#      'https://pragmaticplay-my.sharepoint.com/personal/dmitriy_makashev_pragmaticplay_com/_layouts/15/download.aspx?e=HIIozD&share=ES7fPkUVQ-BNrlLYnC8jF8wBfWMsFPEPgiRkjVsoqHhufQ')
#

print()
