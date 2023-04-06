import requests

API_KEY = 'TÄHÄN API-AVAIN'

city = input('Anna paikkakunta: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp'] - 273.15
    description = weather_data['weather'][0]['description']
    print(f"Sää {city}ssa: {description}, lämpötila {temperature:.1f} astetta Celsius-asteina.")
else:
    print("Säätilan hakeminen epäonnistui.")