# Class Seq for Practice 1.

class Seq:
    """A class for the different methods of the program."""
    def __init__(self, strbases):

        print('New sequence created.')
        self.strbases = strbases

    def len(self):

        return len(self.strbases)

    def comp(self):
        for x in self.strbases:
            complement  =''
            if x == 'A':
                complement += 'T'
            if x == 'T':
                complement += 'A'
            if x == 'G':
                complement += 'C'
            if x == 'C':
                complement += 'G'
        return complement

    def reverse(self):

        reversed = self.strbases[::-1]
        s3 = reversed
        return s3

    def count(self):

        # Counter of the As:
        result_a = 0
        for b in self.strbases:
            if b == 'A':
                result_a += 1
        # Counter of the Ts:
        result_t = 0
        for b in self.strbases:
            if b == 'T':
                result_t += 1
        # Counter of the Gs:
        result_g = 0
        for b in self.strbases:
            if b == 'G':
                result_g += 1
        # Counter of the Cs:
        result_c = 0
        for b in self.strbases:
            if b == 'C':
                result_c += 1
        bases_dict = {'As': result_a, 'Ts': result_t, 'Gs': result_g, 'Cs': result_c}
        return bases_dict

    def perc(self):

        if len(self) > 0:
            perc_a = round(100.0 * count(self)['As'] / len(self), 1)
            perc_t = round(100.0 * count(self)['Ts'] / len(self), 1)
            perc_g = round(100.0 * count(self)['Gs'] / len(self), 1)
            perc_c = round(100.0 * count(self)['Cs'] / len(self), 1)

        else:
            perc_a = 0
            perc_t = 0
            perc_g = 0
            perc_c = 0
        dict_perc = {'As': perc_a, 'Ts': perc_t, 'Gs': perc_g, 'Cs': perc_c}
        return dict_perc

s1 = input('Please, enter Sequence 1:')
str1 = s1.strbases
print('Sequence 1: ', str1)

l1 = s1.len()
print('\tLength: ', l1)

print('Bases Percentage: ', perc(s1))
#d1 = count_bases(s1)
#d2 = count_bases(s2)

s2 = Seq('CGTAAC')
str2 = s2.strbases
print('Sequence 2: ', str2)


print('Bases Percentage: ', perc(s2))

reverse1 = s1.reverse()
print('Sequence 4: ', reversed)
#comp1 = s1.comp()
#print('Sequence 3 {}'.format(comp1))
