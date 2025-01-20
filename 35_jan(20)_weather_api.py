# import requests

# API_KEY = "d1845658f92b31c64bd94f06f7188c9c"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather&quot"

# def get_weather(city):
#     try:
#         params = {
#             "q": city,
#             "appid": API_KEY,
#             "units": "metric"
#         }
#         response = requests.get(BASE_URL, params=params)

#         response.raise_for_status()

#         data = response.json()

#         if data:
#             city_name = data["name"]
#             temperature = data["main"]["temp"]
#             weather_description = data["weather"][0]["description"]
#             humidity = data["main"]["humidity"]
#             wind_speed = data["wind"]["speed"]
       
#             print(f"City: {city_name}")
#             print(f"Temperature: {temperature}°C")
#             print(f"Weather Description: {weather_description}")
#             print(f"Humidity: {humidity}%")
#             print(f"Wind Speed: {wind_speed} m/s")
#         else:
#             print("No data is found for the city")
       
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# city = input("Enter the city name: ")
# get_weather(city)



