# Counting bases.

def count_bases(seq):
    """Counting the number of As in the seq."""

    # Counter of the As:
    result_a = 0
    for b in seq:
        if b == 'A':
            result_a += 1
    # Counter of the Ts:
    result_t = 0
    for b in seq:
        if b == 'T':
            result_t += 1
    # Counter of the Gs:
    result_g = 0
    for b in seq:
        if b == 'G':
            result_g += 1
    # Counter of the Cs:
    result_c = 0
    for b in seq:
        if b == 'C':
            result_c += 1
    bases_dict = {'As': result_a, 'Ts': result_t, 'Gs': result_g, 'Cs': result_c}

    # Return the result:
    return bases_dict


# Main Program:
s = input("Enter the sequence: ").upper()

# Calculate the total sequence length
tl = len(s)
d = count_bases(s)
# Calculate the percentage of As in the sequence
if tl > 0:
    perc_a = round(100.0 * d['As'] / tl, 1)
    perc_t = round(100.0 * d['Ts'] / tl, 1)
    perc_g = round(100.0 * d['Gs'] / tl, 1)
    perc_c = round(100.0 * d['Cs'] / tl, 1)

else:
    perc_a = 0
    perc_t = 0
    perc_g = 0
    perc_c = 0

print("This sequences is: ", tl, 'bases length.')
print('Base A')
print("\tCounter: {}".format(d['As']))
print("\tPercentage: ", perc_a)

print('Base T')
print("\tCounter: {}".format(d['Ts']))
print("\tPercentage: ", perc_t)

print('Base G')
print("\tCounter: {}".format(d['Gs']))
print("\tPercentage: ", perc_g)

print('Base C')
print("\tCounter: {}".format(d['Cs']))
print("\tPercentage: ", perc_c)
