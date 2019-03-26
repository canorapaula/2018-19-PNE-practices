# Example of getting information stored in Chuck Norris' jokes page

import http.client
import json

HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/"
METHOD = "GET"

conn = http.client.HTTPSConnection(HOSTNAME)
headers = {'User-Agent': 'http-client'}


conn.request(METHOD, ENDPOINT + 'count', None, headers)
r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()
user = json.loads(text_json)

number_jokes = user['value']
print("Number of jokes: {}".format(number_jokes))


conn.request(METHOD, '/categories', None, headers)
r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()
user = json.loads(text_json)

categories = user['value']
number_categories = len(user['value'])
print("Names of categories: {}".format(categories))
print("Number of the categories: {}".format(number_categories))


conn.request(METHOD, ENDPOINT + 'random', None, headers)
r3 = conn.getresponse()

text_json = r3.read().decode("utf-8")
conn.close()
user = json.loads(text_json)

joke = user['joke']
print('Random joke: {}'.format(joke))
