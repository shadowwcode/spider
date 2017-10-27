# -*- coding: UTF-8 -*-


import math


def worldStd(num):
    if num < 18.5:
        print '\tYour BMI value is %s, So lean!!!' % num
    elif 18.5 <= num < 25:
        print '\tYour BMI value is %s, Normal' % num
    elif 25 <= num < 30:
        print '\tYour BMI value is %s, Fat!' % num
    else:
        print '\tYour BMI value is %s, So fat!!!' % num



def chinaStd(num):
    if num < 18.5:
        print '\tYour BMI value is %s, So lean!!!' % num
    elif 18.5 <= num < 24:
        print '\tYour BMI value is %s, Normal' % num
    elif 24 <= num < 28:
        print '\tYour BMI value is %s, Fat!' % num
    else:
        print '\tYour BMI value is %s, So fat!!!' % num


if __name__ == '  ':
    height, weight = eval(raw_input('Enter your height and weight, separated of comma: '))
    BMI_value = weight / (height ** 2)
    print 'The international standard is: '
    worldStd(BMI_value)
    print 'The domestic standard is: '
    chinaStd(BMI_value)


if __name__ == ' ':
    def square(x):
        return x * x

    def distance(x1, y1, x2, y2):
        dist = math.sqrt(square(x1 - x2) + square(y1 - y2))
        return dist
    def isTriangle(x1, y1, x2, y2, x3, y3):
        flag = ((x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)) != 0
        return flag

    def sumDiff(x, y):
        sum = x + y
        diff = x - y
        return sum, diff

    def addInterest(balance, rate):
        newBalance = balance * (1 + rate)
        return newBalance

    def test():
        l = [1000, 105, 3500, 739]
        for i in range(len(l)):
            l[i] = addInterest(l[i], 0.05)

        print l



if __name__ == '__main__':
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)

    def reversee(str):
        if str == '':
            return str
        else:
            return reversee(str[1:]) + str[0]

















