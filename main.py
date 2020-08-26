import json
from urllib.request import urlopen
city = input("Enter City Name: ")
mykey = "e0f598fa1262a8b47cf92e164b16256b"
url = "https://openweathermap.org/"
url = url+"data/2.5/weather?appid="
url = url+mykey+f"&q={city}"
response = urlopen(url)
decoded = response.read().decode('utf-8')
data = json.loads(decoded)
for key,value in data.items():
    print(key,value)