file = open('DNA.txt', 'r')
DNA_input = file.read()

print('Total length:', len(DNA_input))

A_counter = 0
G_counter = 0
C_counter = 0
T_counter = 0

for x in DNA_input:
    if x == 'A':
        A_counter += 1
    if x == 'G':
        G_counter += 1
    if x == 'C':
        C_counter += 1
    if x == 'T':
        T_counter += 1

print('A:', A_counter)
print('G:', G_counter)
print('C:', C_counter)
print('T:', T_counter)
