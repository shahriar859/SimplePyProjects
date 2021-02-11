import requests
import json
import sys


location = input()

endPoint = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=bc657163a707c1b10017545da85bb67d&units=metric".format(location)


req = requests.get(endPoint)
res = req.json()

if res is None or res.get("cod") != 200:
	print("Report not available")
	sys.exit()

overview = ", ".join([item.get("main") for item in res.get("weather")])

temp = res.get("main", dict()).get("temp")
humidity = res.get("main", dict()).get("humidity")
temp = res.get("main", dict()).get("temp")

print("\n======================= Weather Report of {} =====================".format(location))
print("Overview: {}".format(overview))
print("Temprature: {} °C".format(temp))
print("Humidity: {}".format(humidity))
print("\n")
