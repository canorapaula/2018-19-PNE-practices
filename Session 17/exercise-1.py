import json
import termcolor

f = open("person.json", 'r')

# Object with all the info
person = json.load(f)

# The end='' is for it to be printed in the same line
for data in person['Person_1']:
    termcolor.cprint("Name: ", 'green', end='')
    print(data['Firstname'], data['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(data['age'])

    termcolor.cprint("Phone Numbers: ", 'green', end='')
    print(len(person['phoneNumber']))
    for i, num in enumerate(person['phoneNumber']):
        termcolor.cprint(" Phone {}".format(i), 'blue', end='')
        print(len(person['phoneNumber']))
        termcolor.cprint("      \n\tType: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("\tNumber: ", 'red', end='')
        print(num['number'])
