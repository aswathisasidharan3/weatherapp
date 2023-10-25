
from django.shortcuts import render,redirect
from geopy.geocoders import Nominatim

from . models import WeatherData
from django.http import JsonResponse
from datetime import datetime,time,timedelta
import requests
import random
import math
import pytz
zones = pytz.all_timezones
# datetime.now(pytz.utc)
# utc = timezone('UTC')
def index(request):
     return render(request, 'index.html')

def prediction(request):
     return render(request, 'prediction.html')
def result(request):
     return render(request, 'result.html')


def result(request):
    
    if request.method == "POST":
        city = request.POST["city"].lower()   
        api_key='c3bd064bdbe667db5bdd5ce43e1b5e4b'
        url1 =f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
        weather_data1 = requests.get(url1).json()
        # print(weather_data1)
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        weather_data = requests.get(url).json()
        # print(weather_data)
        # city='kannur'
        url_api=f"http://127.0.0.1:8000/app_api/all/?city={city}"
        api_data=requests.get(url_api).json()
        for entry in api_data:
           if entry['city'] == city:
             
             print(f"Weather in {city}:")
             print(f"Temperature: {entry['temp']}°C")
             print(f"Temp_max: {entry['temp_max']}°C")
             print(f"Temp_min: {entry['temp_min']}°C")
             print(f"pressure: {entry['pressure']}mb")
             print(f"humidity: {entry['humidity']}%")
             print(f"wind: {entry['wind']}km/h")

    
             print(f"description: {entry['description']}")
             
             break
        else:
           print(f"No weather data found for {city}")

        
        # forecast_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={api_key}"
        

    
        try:
            context = {
                ####
                "city":weather_data1["city"]["name"],
                # "city_country":weather_data1["city"]["country"],
                # "wind":weather_data1['list'][0]['wind']['speed'],
                "wind":entry['wind'],
                "description":entry['description'],
                "degree":weather_data1['list'][0]['wind']['deg'],
                # 'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                "cloud":weather_data1['list'][0]['clouds']['all'],
                # "timestamp":weather_data1["dt"],

                # "date_time":weather_data1['list'][0]["dt_txt"],
                'date_time': datetime.now().strftime("%d %b %Y | %I:%M:%S %p"),
               "date_time1":weather_data1['list'][1]["dt_txt"],
                # 'date_time1':datetime.now().strftime("%d %b %Y | %I:%M:%S %p"),
                'date_time2':weather_data1['list'][2]["dt_txt"],
                'date_time3':weather_data1['list'][3]["dt_txt"],
                'date_time4':weather_data1['list'][4]["dt_txt"],
                'date_time5':weather_data1['list'][5]["dt_txt"],
                'date_time6':weather_data1['list'][6]["dt_txt"],
                'date_time7':weather_data1['list'][7]["dt_txt"],
                'date_time8':weather_data1['list'][8]["dt_txt"],
                'date_time9':weather_data1['list'][9]["dt_txt"],
                'date_time16':weather_data1['list'][16]["dt_txt"],
                 'date_time24':weather_data1['list'][24]["dt_txt"],
                 'date_time32':weather_data1['list'][32]["dt_txt"],
                #  'date_time40':weather_data1['list'][40]["dt_txt"],
                # "temp": round(weather_data1["list"][0]["main"]["temp"] -273.0),
                "temp":entry['temp'],
                "temp_max":entry['temp_max'],
                "temp_min":entry['temp_min'],

                 "feels_like": round(weather_data1["list"][0]["main"]["feels_like"] -273.0),
                "temp_min1":math.floor(weather_data1["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(weather_data1["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(weather_data1["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(weather_data1["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(weather_data1["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(weather_data1["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(weather_data1["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(weather_data1["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(weather_data1["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(weather_data1["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(weather_data1["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(weather_data1["list"][6]["main"]["temp_max"] -273.0),
                "temp_max7": math.ceil(weather_data1["list"][7]["main"]["temp_max"] -273.0),
                "temp_min7":math.floor(weather_data1["list"][7]["main"]["temp_min"] -273.0),
                "temp_max8": math.ceil(weather_data1["list"][8]["main"]["temp_max"] -273.0),
                "temp_min8":math.floor(weather_data1["list"][8]["main"]["temp_min"] -273.0),
                "temp_max8": math.ceil(weather_data1["list"][9]["main"]["temp_max"] -273.0),
                "temp_min16":math.floor(weather_data1["list"][16]["main"]["temp_min"] -273.0),
                "temp_max16": math.ceil(weather_data1["list"][16]["main"]["temp_max"] -273.0),
                 "temp_min24":math.floor(weather_data1["list"][24]["main"]["temp_min"] -273.0),
                "temp_max24": math.ceil(weather_data1["list"][24]["main"]["temp_max"] -273.0),
                "temp_min32":math.floor(weather_data1["list"][32]["main"]["temp_min"] -273.0),
                "temp_max32": math.ceil(weather_data1["list"][32]["main"]["temp_max"] -273.0),
                #  "temp_min40":math.floor(weather_data1["list"][40]["main"]["temp_min"] -273.0),
                # "temp_max40": math.ceil(weather_data1["list"][40]["main"]["temp_max"] -273.0),
                
                 "grnd_level":weather_data1["list"][0]["main"]["grnd_level"],
                 "pressure":entry['pressure'],
                 "humidity":entry['humidity'],

                # "pressure":weather_data1["list"][0]["main"]["pressure"],
                # "humidity":weather_data1["list"][0]["main"]["humidity"], 
                "wind8":weather_data1['list'][8]['wind']['speed'],
                "humidity8":weather_data1["list"][8]["main"]["humidity"], 
                "wind16":weather_data1['list'][16]['wind']['speed'],
                "humidity16":weather_data1["list"][16]["main"]["humidity"], 
                "wind24":weather_data1['list'][24]['wind']['speed'],
                "humidity24":weather_data1["list"][24]["main"]["humidity"], 
                 "wind32":weather_data1['list'][32]['wind']['speed'],
                "humidity32":weather_data1["list"][32]["main"]["humidity"], 
                #  "wind40":weather_data1['list'][40]['wind']['speed'],
                # "humidity40":weather_data1["list"][40]["main"]["humidity"], 
                # "rain":weather_data1["list"][0]["main"]["rain"],
                # "rain":weather_data1["list"][1]["weather"][0]["rain"],

                "weather":weather_data1["list"][1]["weather"][0]["main"],
                # "description":weather_data1["list"][1]["weather"][0]["description"],
                # "icon":weather_data1["list"][0]["weather"][0]["icon"],
                "icon1":weather_data1["list"][1]["weather"][0]["icon"],
                "icon2":weather_data1["list"][2]["weather"][0]["icon"],
                "icon3":weather_data1["list"][3]["weather"][0]["icon"],
                "icon4":weather_data1["list"][4]["weather"][0]["icon"],
                "icon5":weather_data1["list"][5]["weather"][0]["icon"],
                "icon6":weather_data1["list"][6]["weather"][0]["icon"],
                "icon7":weather_data1["list"][7]["weather"][0]["icon"],
                "icon8":weather_data1["list"][8]["weather"][0]["icon"],
                "icon9":weather_data1["list"][9]["weather"][0]["icon"],
                "icon16":weather_data1["list"][16]["weather"][0]["icon"],
                "icon24":weather_data1["list"][24]["weather"][0]["icon"],
                "icon32":weather_data1["list"][32]["weather"][0]["icon"],
                #   "icon40":weather_data1["list"][40]["weather"][0]["icon"],
                "description1":weather_data1["list"][1]["weather"][0]["description"],
                "description2":weather_data1["list"][2]["weather"][0]["description"],
                "description3":weather_data1["list"][3]["weather"][0]["description"],
                "description4":weather_data1["list"][4]["weather"][0]["description"],
                "description5":weather_data1["list"][5]["weather"][0]["description"],
                "description8":weather_data1["list"][8]["weather"][0]["description"],
                "description16":weather_data1["list"][16]["weather"][0]["description"],
                "description24":weather_data1["list"][24]["weather"][0]["description"],
                "description32":weather_data1["list"][32]["weather"][0]["description"],
                "description24":weather_data1["list"][24]["weather"][0]["description"],
            }

         
        
        except:
            context = {

            "city":"Not Found, Check your spelling..."
        }

        return render(request, "result.html", context)
    else:
        return redirect('index')
from app_api.models import WeatherData
# forecasr_url=f"http://127.0.0.1:8000/app_api/?city=kannur"
# forecast_data=api_data=requests.get(forecasr_url).json()
forecast_data = WeatherData.objects.filter(city='kannur')  # Filter data by city.


import random
from datetime import datetime, timedelta
from app_api.models import WeatherData  # Import the WeatherData model from your Django app

# Assuming the WeatherData model has fields like 'temp', 'temp_max', 'temp_min', 'humidity', 'pressure', and 'date'

city = 'kannur'

# Calculate the start and end date for the next 5 days
current_date = datetime.now().date()
end_date = current_date + timedelta(days=5)

# Filter data by city and date range
forecast_data = WeatherData.objects.filter(city=city, date__range=(current_date, end_date))

# Initialize lists for historical data
historical_temp = []
historical_temp_max = []
historical_temp_min = []
historical_humidity = []
historical_pressure = []

# Iterate through forecast data and append values to the historical lists
for entry in forecast_data:
    historical_temp.append(entry.temp)
    historical_temp_max.append(entry.temp_max)
    historical_temp_min.append(entry.temp_min)
    historical_humidity.append(entry.humidity)
    historical_pressure.append(entry.pressure)

def predict_weather(historical_temp, historical_temp_max, historical_temp_min, historical_pressure, historical_humidity):
    avg_temp = sum(historical_temp) / len(historical_temp)
    avg_temp_max = sum(historical_temp_max) / len(historical_temp_max)
    avg_temp_min = sum(historical_temp_min) / len(historical_temp_min)
    avg_pressure = sum(historical_pressure) / len(historical_pressure)
    avg_humidity = sum(historical_humidity) / len(historical_humidity)
    
    # Initialize lists for predicted values for each day
    predicted_temperatures = []
    predicted_temp_max_values = []
    predicted_temp_min_values = []
    predicted_humidity_values = []
    predicted_pressure_values = []
    
    for _ in range(5):  # Predict for the next 5 days
        temp_fluctuation = random.uniform(-2, 2)
        temp_max_fluctuation = random.uniform(-2, 2)
        temp_min_fluctuation = random.uniform(-2, 2)
        humidity_fluctuation = random.uniform(-5, 5)
        pressure_fluctuation = random.uniform(-2, 2)
        
        predicted_temp = avg_temp + temp_fluctuation
        predicted_temp_max = avg_temp_max + temp_max_fluctuation
        predicted_temp_min = avg_temp_min + temp_min_fluctuation
        predicted_humidity = avg_humidity + humidity_fluctuation
        predicted_pressure = avg_pressure + pressure_fluctuation
        
        predicted_temperatures.append(predicted_temp)
        predicted_temp_max_values.append(predicted_temp_max)
        predicted_temp_min_values.append(predicted_temp_min)
        predicted_humidity_values.append(predicted_humidity)
        predicted_pressure_values.append(predicted_pressure)
        
        # Update the averages for the next iteration (for the next day)
        avg_temp = predicted_temp
        avg_temp_max = predicted_temp_max
        avg_temp_min = predicted_temp_min
        avg_humidity = predicted_humidity
        avg_pressure = predicted_pressure
        

    
    return predicted_temperatures, predicted_temp_max_values, predicted_temp_min_values, predicted_humidity_values, predicted_pressure_values

predicted_temperatures, predicted_temp_max_values, predicted_temp_min_values, predicted_humidity_values, predicted_pressure_values = predict_weather(
    historical_temp, historical_temp_max, historical_temp_min, historical_pressure, historical_humidity)
for day in range(5):
    print(f"Day {day + 1} Predictions:")
    print(f"Predicted Temperature: {predicted_temperatures[day]:.1f}°C")
    print(f"Predicted Max Temperature: {predicted_temp_max_values[day]:.1f}°C")
    print(f"Predicted Min Temperature: {predicted_temp_min_values[day]:.1f}°C")
    print(f"Predicted Humidity: {predicted_humidity_values[day]:.1f}%")
    print(f"Predicted Pressure: {predicted_pressure_values[day]:.1f} hPa")
    print("-" * 20)

# You can use the predicted values for the next 5 days for further processing or display.
# 