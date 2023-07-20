import requests

def converter_kelvintocelcius(kelvin):
    return kelvin - 273.15

#INPUT typed weather
def openweathermap_inputWeather():
	openweathermap_apiKey = "OPENWEATHERMAPAPIKEY"
	
	lon = input("Longitude: ")
	lat = input("Latitude: ")
	baseUrl = "https://api.openweathermap.org/data/2.5/weather"
	openweathermap_url = f"{baseUrl}?lat={lat}&lon={lon}&appid={api_key}"
	openweathermap_response = requests.get(baseUrl)
	data = openweathermap_response.json()

	print(f"Location: {data['name']}")
	print(f"Tempature: {converter_kelvintocelcius(data['main']['temp']):.2f} Celsius")
	print(f"Humidity: {data['main']['humidity']}%")

		