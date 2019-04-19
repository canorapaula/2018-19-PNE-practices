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

listspecies1()
blep = listspecies1().split(',')
termcolor.cprint('BLEP {}'.format(blep), 'yellow')

if blep in LINK:
    SPECIE = blep
    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection(HOSTNAME)

    termcolor.cprint('SPECIE {}'.format(SPECIE), 'green')

    conn.request(METHOD, HOSTNAME + ENDPOINT + ENDPOINT2 + SPECIE + ENDPOINT3, None, headers)
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")
    conn.close()
    user = json.loads(text_json)
    termcolor.cprint('LINK {}'.format(HOSTNAME + ENDPOINT + ENDPOINT2 + SPECIE + ENDPOINT3), 'green')
    for k in user['karyotype']:
        print('K', k)
