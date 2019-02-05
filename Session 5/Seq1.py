class Seq:
    """A class for representing sequences."""
    def __init__(self, strbases):
        print('New sequence created.')

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq
    All the objects of the class Gene will
    inheritage the methods from Seq Class"""
    pass


s1 = Gene("ATTCGATCC")
s2 = Seq("AAAGG")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("Sequence 1:", str1)
print(" Length: {}".format(l1))
print("Sequence 2: {}".format(str2))
print(' Length', l2)

print("\nThe end")
