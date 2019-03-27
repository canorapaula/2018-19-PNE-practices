# Example of getting information about the weather of
# a location

import http.client
import json

place = input('Place')
def get_woeid(place):
    HOSTNAME = "www.metaweather.com"
    ENDPOINT = "/api/location/search/?query="
    ENDPOINT += place
    METHOD = "GET"

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request(METHOD, ENDPOINT + '/', None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")
    conn.close()
    list_dataplace = json.loads(text_json)
    return list_dataplace


city_data = get_woeid(place)
woeid = city_data[0]['woeid']
print(woeid)
"""
time = weather['time']

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = input('Please, introduce a capital: ')

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
"""
