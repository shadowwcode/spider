# -*- coding: UTF-8 -*-


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


if __name__ == '__main__':
    height, weight = eval(raw_input('Enter your height and weight, separated of comma: '))
    BMI_value = weight / (height ** 2)
    print 'The international standard is: '
    worldStd(BMI_value)
    print 'The domestic standard is: '
    chinaStd(BMI_value)

























