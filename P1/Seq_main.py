# Main program for Practice 1
# In this program the output will be printed:

from P1.Seq import Seq                                  # It doesn't work?!?!?!

s1 = input('Please, enter Sequence 1: ')
# str1 = s1.strbases
print('Sequence 1: ', s1)
s1 = str(s1)
l1 = s1.length(s1)
print('\tLength: ', l1)
b1 = s1.count()
print('\tBases count: {}'.format(b1))
p1 = s1.perc()
print('\tBases percentage: {}'.format(p1))

s2 = input('Please, enter Sequence 2: ')
str2 = s2.strbases
print('Sequence 2: ', str2)
l2 = s2.length()
print('\tLength: ', l2)
b2 = s2.count()
print('\tBases count: {}'.format(b2))
p2 = s2.perc()
print('\tBases percentage:{}'.format(p2))
