# Open the file and have access to this person's info

import json
import termcolor

f = open("person.json", 'r')

# Object with all the info
person = json.load(f)

print()
# The end='' is for it to be printed in the same line
termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname1'], person['Lastname1'])
termcolor.cprint("Age: ", 'green', end='')
print(person['age1'])

termcolor.cprint("Phone Numbers: ", 'green', end='')
print(len(person['phoneNumber1']))
for i, num in enumerate(person['phoneNumber1']):
    termcolor.cprint(" Phone {}".format(i), 'blue', end='')
    print(len(person['phoneNumber1']))
    termcolor.cprint("      \n\tType: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("\tNumber: ", 'red', end='')
    print(num['number'])
print()

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname0'], person['Lastname0'])
termcolor.cprint("Age: ", 'green', end='')
print(person['age0'])

termcolor.cprint("Phone Numbers: ", 'green', end='')
print(len(person['phoneNumber0']))
for i, num in enumerate(person['phoneNumber0']):
    termcolor.cprint(" Phone {}".format(i), 'blue', end='')
    print(len(person['phoneNumber0']))
    termcolor.cprint("      \n\tType: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("\tNumber: ", 'red', end='')
    print(num['number'])
print()

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname2'], person['Lastname2'])
termcolor.cprint("Age: ", 'green', end='')
print(person['age2'])

# With the i you have the index and the enumerate is the function for counting
termcolor.cprint("Phone Numbers: ", 'green', end='')
print(len(person['phoneNumber2']))
for i, num in enumerate(person['phoneNumber2']):
    termcolor.cprint(" Phone {}".format(i), 'blue', end='')
    termcolor.cprint("      \n\tType: ", 'red', end='')
    print(num['type'])
    termcolor.cprint("\tNumber: ", 'red', end='')
    print(num['number'])
