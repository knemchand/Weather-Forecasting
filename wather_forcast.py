import requests

city = input("Enter city: ")
while not city:
    city = input("Enter city: ")
try:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric")
    if response.status_code == 200:
        main_item = response.json()
        print(f"Temperature: {main_item['main']['temp']} Cal")
        print(f"Min Temmperature: {main_item['main']['temp_min']} Cal")
        print(f"Max Temperature: {main_item['main']['temp_max']} Cal")
        print(f"Humidity: {main_item['main']['humidity']}%")
    else:
        print("Invalid city name..!")
except Exception as e: print(e)