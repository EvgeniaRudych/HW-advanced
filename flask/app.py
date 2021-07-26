# flask_web/app.py
import json

from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    cities_list = request.form.getlist('city')

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    weathers = []

    for city in cities_list:
        querystring = {"q": city, "cnt": "1", "mode": "null", "type": "link, accurate", "units": "metric"}

        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            print(data)
            weathers.append(data['list'][0])

    if len(weathers) > 0:
        return render_template("weathers.html", weathers=weathers)

    return Response(status=404)


@app.route('/search_lon_lat', methods=['POST'])
def search_lon_lat():
    lon = request.form.get("lon")
    lat = request.form.get("lat")
    querystring = {"q": "", "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                   "units": "metric"}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        weather = data['list'][0]
        return render_template("weather.html", weather=weather)

    return Response(status=404)


api = Api(app)

todos = {}


class Todo(Resource):

    def get(self, todo_id):
        try:
            data = {todo_id: todos[todo_id]}
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get('text')
        data = {todo_id: todos[todo_id]}
        with open('todos.json', 'w') as write_file:
            json.dump(data, write_file)
        write_file.close()
        return data

    def delete(self, todo_id):
        del todos[todo_id]
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        return todos

    def post(self):
        todos[request.json.get('todo_id', None)] = request.json.get('text', "")
        return todos


class WeatherAPI(Resource):
    def get(self):
        city = request.args.get("city")
        querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                       "units": "metric"}

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }
        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            if len(data['list']) > 0:
                weather = data['list'][0]
                return render_template("weather.html", weather=weather)

        return Response(status=404)


api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(WeatherAPI, '/weather')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
