import requests
import json

weather = requests.get('https://api.weather.gov/gridpoints/MFL/110,66/forecast')
#parsedw = json.loads(weather.json())
#print(json.dumps(parsedw, indent=4))
#print(f'\n\n\n {weather.json()}')
#print(json.dumps(weather.json()["properties"]["periods"], indent=2))
hourly = weather.json()["properties"]["periods"]
#print(type(hourly))
print(json.dumps(hourly[0]["name"], indent=2))
#hour1 = weather.json["properties"]["periods"]
#print(hour1)