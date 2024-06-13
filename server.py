from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    cities = ['Cape Town', 'New York', 'Brazil']
    weather_data = []

    appid = '5d122ae919d3619fb527552f116cff0e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'

    for city in cities:
        PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL, params=PARAMS)
        res = r.json()

        weather = {
            'city': city,
            'condition': res['weather'][0]['main'],
            'description': res['weather'][0]['description'],
            'temp': res['main']['temp']
        }
        weather_data.append(weather)

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
