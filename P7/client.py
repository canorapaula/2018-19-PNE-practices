import http.client
import http.server
import json
import termcolor

HOSTNAME = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000139618?content-type=application/json"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json)

sequence = user['seq']
len_sequence = len(sequence)

termcolor.cprint('The number of bases of the sequence is: {}'.format(len_sequence), 'green')

A_number = 0
C_number = 0
T_number = 0
G_number = 0
for x in sequence:
    if x == 'A':
        A_number += 1
    elif x == 'C':
        C_number += 1
    elif x == 'T':
        T_number += 1
    elif x == 'G':
        G_number += 1

termcolor.cprint('The number of T bases of the sequence is: {}'.format(T_number), 'green')

percentages = ''
if len_sequence > 0:
    per_A = round(100.0 * A_number / len_sequence, 1)
    percentages = percentages + ''.format(per_A)
    per_C = round(100.0 * C_number / len_sequence, 1)
    percentages = percentages + ''.format(per_C)
    per_T = round(100.0 * T_number / len_sequence, 1)
    percentages = percentages + ''.format(per_C)
    per_G = round(100.0 * G_number / len_sequence, 1)
    percentages = percentages + ''.format(per_G)

else:
    per_A = 0
    per_C = 0
    per_G = 0
    per_T = 0

termcolor.cprint('The percentage of A bases of the sequence is: {}%'.format(per_A), 'green')
termcolor.cprint('The percentage of C bases of the sequence is: {}%'.format(per_C), 'green')
termcolor.cprint('The percentage of T bases of the sequence is: {}%'.format(per_T), 'green')
termcolor.cprint('The percentage of G bases of the sequence is: {}%'.format(per_G), 'green')
