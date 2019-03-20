import json
import termcolor

f = open("person.json", 'r')

person = json.load(f)

print("Total people in the database:", len(person))

for data in person:
    termcolor.cprint("Name: ", 'green', end='')
    print(data['Firstname'], data['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(data['age'])
    phones = data['phoneNumber']
    termcolor.cprint("Phone Numbers: ", 'green', end='')
    print(len(phones))
    for i, num in enumerate(data['phoneNumber']):
        termcolor.cprint(" Phone {}".format(i), 'blue', end='')
        termcolor.cprint("\n\tType: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("\tNumber: ", 'red', end='')
        print(num['number'])
    print()
