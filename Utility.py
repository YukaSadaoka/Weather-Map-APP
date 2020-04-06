import requests
import os

def getWeather(city=None):
    try:
        params_weather = {'APPID': os.getenv('WEATHER_APIKEY'), 'q': city, 'units': 'metric'}
        return requests.get(os.getenv('WEATHER_ENDPOINT'), params=params_weather)
    except:
        print("Exception thrown in getWether()\n")
        return str("Error occurred. Try again.")

def createLocationParam(response=None):
    try:
        if response is not None:
            dctParam = {'center': f"{response['name']}",'size': '600x400', 'key': os.getenv('GOOGLE_APIKEY'), 'zoom': 13}
            return dctParam
        else:
            return str('Error occurred during retrieving data.')
    except:
        print('Exception thrown in createLocationParam')
        return str('Error occurred during retrieving data.')

def format_response(weatherData=None):
    try:
        if weatherData is not None:
            name = weatherData['name']
            desc = weatherData['weather'][0]['description']
            currentTemp = weatherData['main']['temp']
            high = weatherData['main']['temp_max']
            low = weatherData['main']['temp_min']

            final = f"{str(name)}"
            final += f"\nNow: {str(currentTemp)}°C"
            final += f"High: {str(high)}°C  Low: {str(low)}°C\n{str(desc)}"
            return final
        return str("There was a problem during\nretrieving information.")
    except:
        return str("There was a problem during\nretrieving information.")



