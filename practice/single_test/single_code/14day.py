# -*- coding: UTF-8 -*-

# 50
import random


# 46
def getSq(num):
    return num * num

def getSeq():
    while True:
        x = int(raw_input('Input a number: '))
        if getSq(x) <= 50:
            print 'The square of number is %d.' % (getSq(x))
        else:
            break

# 50
print '<----------50------------->'
print random.random()
print random.uniform(10, 20)
print random.randint(10, 20)


# 51
print '<----------51------------->'
if __name__ == '__main__':
    a = 077
    b = a & 3
    print b
    print 'a & b = %d' % b
    b &= 7
    print b
    print 'a & b = %d' % b
""" binary  & ^ << >> | """











