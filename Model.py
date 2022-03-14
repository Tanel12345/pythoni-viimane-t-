
import requests

import time


class Model:

    def __init__(self):
        self.vastus = 'Tulemus'

    def get_weather_data(self, value):
        self.value = value.title()

        if self.value:

            api = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={self.value}&appid=ebac28585dfb7b6501dff19ff718931b")

            if api.json()['cod'] == '404':
                self.vastus = "Tegemist ei ole õige linna nimega," + "\n" + " proovi uuesti: "
            else:

                weather = api.json()['weather'][0]['main']
                temp = api.json()['main']['temp']
                celsiustemp = (temp-32) / 1.8

                temp1 = int(api.json()['main']['temp'] - 273.15)
                self.vastus = "Temperatuur asukohas " + self.value + " On " + \
                    str(temp1) + " kraadi C" + "\n" + "Pilvisus on " + weather
