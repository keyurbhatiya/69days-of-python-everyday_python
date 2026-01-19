# Real time weather tracker

import requests

def get_weather(city):
    api_key = "your_wether_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    metric = "metric"

    # parameters

    parameters = {
        'q' : city,
        'appid' : api_key,
        "units" : metric
    }

    try : 
        response = requests.get(base_url, params=parameters)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            print(f" \n ---- Weather in {city.capitalize()}---")
            print(f"Temperature : {temp}c")
            print(f"Condition : {desc.capitalize()}")
            print(f"Humidity : {humidity}%")

        else:
            print(f"Error : {data['message']}")
    except Exception as e:
        print(f"An error occurred : {e}")

city_input = input("Enter city name : ")
get_weather(city_input)