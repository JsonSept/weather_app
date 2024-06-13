from flask import Flask, render_template
import requests
# import pytz
from datetime import datetime
from zoneinfo import ZoneInfo
# from time import gmtime, strftime
app = Flask(__name__)

tranlations = {
    "cape town": "johannesburg",
    "brazil" : "gmt+3",
    "london" : "london"
}

def getCityTime(city):
    # print(tranlations)
    city = tranlations.get(city.lower()) if tranlations.get(city.lower()) else city; 
    print(city)
    city = '_'.join(city.split(' '))
    url = "http://worldtimeapi.org/api/timezone"
    resp = requests.get(url)
    data = resp.json() 
    
    for c in range( len(data) ):
        if city.lower() in data[c].lower():
            break 
    
    url = f'{url}/{data[c]}'
    resp = requests.get(url)
    return resp.json() 

@app.route('/')


def home():
    # londonTime = getCityTime("london")['datetime']
    current_datetime = datetime.now().date()
    date_part = current_datetime.strftime("%d %B %Y")
    # time_part = current_datetime.strftime("%H:%M")
    # formatted_time = strftime("%Y-%m-%d %H:%M")
    cities = ['Cape Town', 'New York', 'Brazil', 'London']
    weather_data = []

    appid = '5d122ae919d3619fb527552f116cff0e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    for city in cities:
        PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL, params=PARAMS)
        res = r.json()
        
        # city_zone = ZoneInfo(city)
        # city_time = datetime.now(city_zone)
        weather = {
            'city': city,
            # 'time': datetime.fromtimestamp(res["dt"]),
            'condition': res['weather'][0]['main'],
            'description': res['weather'][0]['description'],
            'temp': res['main']['temp'],
            'time': getCityTime(city)['datetime'].split("T")[1].split('.')[0],
            # 'date': getCityTime(city)['datetime'].split("T")[0]
                # my_date = datetime.date(2023, 5, 17)
        }

        weather_data.append(weather)
    
    return render_template('index.html', weather_data=weather_data,date_part=date_part)

if __name__ == '__main__':
    app.run(debug=True)
