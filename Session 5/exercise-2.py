# Exercise 2, calculating info for 2 sequences.

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
s1 = input("Enter the sequence 1: ").upper()
s2 = input("Enter the sequence 2: ").upper()

# Calculate the total sequence length
tl1 = len(s1)
tl2 = len(s2)
d1 = count_bases(s1)
d2 = count_bases(s2)
# Calculate the percentage of letters in the sequence 1
if tl1 > 0:
    perc_a = round(100.0 * d1['As'] / tl1, 1)
    perc_t = round(100.0 * d1['Ts'] / tl1, 1)
    perc_g = round(100.0 * d1['Gs'] / tl1, 1)
    perc_c = round(100.0 * d1['Cs'] / tl1, 1)

else:
    perc_a = 0
    perc_t = 0
    perc_g = 0
    perc_c = 0

# Calculate the percentage of letters in the sequence 2
if tl1 > 0:
    perc_a = round(100.0 * d2['As'] / tl2, 1)
    perc_t = round(100.0 * d2['Ts'] / tl2, 1)
    perc_g = round(100.0 * d2['Gs'] / tl2, 1)
    perc_c = round(100.0 * d2['Cs'] / tl2, 1)

else:
    perc_a = 0
    perc_t = 0
    perc_g = 0
    perc_c = 0

# You could also do it with a list:
# seq_list = [s1, s2]
# for i+1, elem in enumerate(seq_list)
# for i(index) + 1,elem(element) in enumerate(list)


# For sequence 1:
print("\nSquence 1 is: ", tl1, 'bases length.')
print('Base A')
print("\tCounter: {}".format(d1['As']))
print("\tPercentage: ", perc_a)

print('Base T')
print("\n\tCounter: {}".format(d1['Ts']))
print("\tPercentage: ", perc_t)

print('Base G')
print("\tCounter: {}".format(d1['Gs']))
print("\tPercentage: ", perc_g)

print('Base C')
print("\tCounter: {}".format(d1['Cs']))
print("\tPercentage: ", perc_c)

# For sequence 2:
print("\nSequence 2 is: ", tl2, 'bases length.')
print('Base A')
print("\tCounter: {}".format(d2['As']))
print("\tPercentage: ", perc_a)

print('Base T')
print("\tCounter: {}".format(d2['Ts']))
print("\tPercentage: ", perc_t)

print('Base G')
print("\tCounter: {}".format(d2['Gs']))
print("\tPercentage: ", perc_g)

print('Base C')
print("\tCounter: {}".format(d2['Cs']))
print("\tPercentage: ", perc_c)
