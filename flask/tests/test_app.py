from tests.conftest import client
import requests
from unittest import mock
from config import Config


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "65d8df904bmsh6d48a89e82cd263p1eccd5jsnf61ac5deb725"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"city": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


class ApiMock:
    def __init__(self, *args, **kwargs):
        self.weather_mock = {"message": "accurate",
                             "cod": "200",
                             "count": 1,
                             "list":
                                 [{"id": 703448,
                                   "name": "Kyiv",
                                   "coord":
                                       {"lat": 50.4333, "lon": 30.5167},
                                   "main": {"temp": 300.95,
                                            "feels_like": 301.38,
                                            "temp_min": 299.82,
                                            "temp_max": 26.67,
                                            "pressure": 1019,
                                            "humidity": 50},
                                   "dt": 1624111746,
                                   "wind": {"speed": 4, "deg": 120},
                                   "sys": {"country": "UA"},
                                   "rain": None,
                                   "snow": None,
                                   "clouds": {"all": 0},
                                   "weather": [{"id": 800,
                                                "main": "Clear",
                                                "description": "clear sky",
                                                "icon": "01d"}]}]}
        self.status_code = 200

    def json(self):
        return self.weather_mock


def test_mock_search_weather(client, mocker):
    mocker.patch('requests.request', side_effect=ApiMock)
    response = client.post("/search", data={"cities": "Kiev"})
    print(response)
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for Kiev" in response.data
