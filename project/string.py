

# months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
#
# val = int(raw_input('Input a number(1~12): '))
# print(months[(val-1)*3:val*3])

def get_month(num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if 1 <= int(num) <=12:
        return months[num-1]
    else:
        print 'Error'

if __name__ == '  ':

    for i in range(1, 13):
        print get_month(i)



##  yuan zhou lv

from random import random
from time import clock
from math import sqrt

DARTS = 2**10
hits = 0
clock()
for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1

pi = 4 * (float(hits) / DARTS)

print 'Pi = %s' % pi
print 'Time: %-5.5ss' % clock()


















