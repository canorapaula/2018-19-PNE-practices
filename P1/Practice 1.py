class Seq:
    """A class for the different methods of the program."""
    def __init__(self, strbases):
        print('New sequence created.')
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def comp(self):
        for x in self.strbases:
            if x == 'A':
                print('T')
            if x == 'T':
                print('A')
            if x == 'G':
                print('C')
            if x == 'C':
                print('G')
        
        return complement

s1 = Seq('AAATTTGGGCCC')
str1 = s1.strbases
print('The sequence is: ', str1)

l1 = s1.len()
print('\tLength: ', l1)

comp1 = s1.comp()
print('The complement is {}'.format(comp1))
