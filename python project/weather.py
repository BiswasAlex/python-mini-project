import requests 
#module to send request to API

API_KEY = "388cf5895832ff9f362cadf2b91f9314"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name:")
request_url= f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code==200:
    data = response.json()
    weather = data['weather'] [0]['description']
    
    temperature = round(data["main"]["temp"] - 273.15, 2)
    
    print("weather:", weather)
    print("temperature:", temperature, "celsius")
else:
    print("Api did not work.")