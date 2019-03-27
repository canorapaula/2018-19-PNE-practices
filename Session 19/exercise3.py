# Example of getting information stored in github for Exercise 3

import http.client
import json
import termcolor

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = "Obijuan"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)
r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()
user = json.loads(text_json)

# For the name...
name = user['name']
print()
termcolor.cprint("User's real Name: ", 'yellow', end = '')
print(name)

# For the repos' list...
conn.request(METHOD, ENDPOINT + GITHUB_ID + '/repos', None, headers)
r2 = conn.getresponse()

text_json = r2.read().decode("utf-8")
conn.close()
user = json.loads(text_json)

termcolor.cprint("List of Repos: ", 'yellow')
for x in user:
    print('\t', end = '')
    print(x['name'])

# For the total number of commits to the 2018-19-PNE-repo...
conn.request(METHOD, ENDPOINT + '/repos/' + GITHUB_ID + '/2018-19-PNE-practices/contributors', None, headers)
r3 = conn.getresponse()

text_json = r3.read().decode("utf-8")
conn.close()
user = json.loads(text_json)

ncontributions = user['contributions']
termcolor.cprint("Total number of commits to the 2018-19-PNE-repo: ", 'yellow', end = '')
print(ncontributions)
