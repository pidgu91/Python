import requests


class City:
    def __init__(self, city, lat, lon, units="metric"):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=ebed93b4659855e42927a25bc7fdbf68')

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]

    def print_weather(self):
        if self.units == "metric":
            print(f"In {self.city} it is: {self.temp} degrees celsius ")
            print(f"Today's High: {self.temp_max} degrees celsius ")
            print(f"Today's Low: {self.temp_min} degrees celsius ")
        elif self.units == "imperial":
            print(f"In {self.city} it is: {self.temp} degrees fahrenheit ")
            print(f"Today's High: {self.temp_max} degrees fahrenheit ")
            print(f"Today's Low: {self.temp_min} degrees fahrenheit ")


# my_city = City("Tokyo", "35.69", "139.69", "metric")
# my_city.print_weather()

vacation_city = City("Portland", "45.5152", "-122.6784", "imperial")
vacation_city.print_weather()
