import http.client
import json
import termcolor
from list_species_ensembl import listspecies1

LINK = 'http://rest.ensembl.org/info/assembly/homo_sapiens?content-type=application/json'
HOSTNAME = "rest.ensembl.org"
ENDPOINT = "/info/"
ENDPOINT2 = "assembly/"
SPECIE = ''
ENDPOINT3 = "?content-type=application/json"
METHOD = "GET"

blep = listspecies1()
for x in blep:
    if x in LINK:
        SPECIE = x
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection(HOSTNAME)

        conn.request(METHOD, ENDPOINT + ENDPOINT2, None, headers)
        r1 = conn.getresponse()
        text_json = r1.read().decode("utf-8")
        conn.close()
        user = json.loads(text_json)

        for x in user['karyotype']:
            print('X', x)