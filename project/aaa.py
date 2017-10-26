
import math
import sys

if __name__ == '  ':
    from turtle import *
    def curvemove():
        for i in range(200):
            right(1)
            forward(1)
    color('red','pink')
    begin_fill()
    left(140)
    forward(111.65)
    curvemove()
    left(120)
    curvemove()
    forward(111.65)
    end_fill()
    done()


if __name__ == '  ':

    def main():
        a, b, c = eval(raw_input('Please enter the coefficients(a, b, c): '))
        # try:
        #     discRoot = math.sqrt(b ** 2 - 4 * a * c)
        # except:
        #     print 'Error! No real roots'
        #     sys.exit(0)

        delta = b ** 2 - 4 * a * c
        if a == 0:
            root = -c / float(b)
            print '\nThere is an solution', root
        elif delta == 0:
            root = float(- b) / (2 * a)
            print '\nThe solution is ', root
        elif delta > 0:
            discRoot = math.sqrt(delta)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            print '\nThe solutions are: ', root1, root2
        else:
            print 'Error! No real roots'

    main()

if __name__ == '  ':

    def main():
        print 'This program finds the real solution to a quadratic\n'
        try:
            a, b, c = eval(raw_input('Please enter the coefficients(a, b, c): '))
            discRoot = math.sqrt(b ** 2 - 4 * a * c)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            if root1 == root2:
                print '\nThe solution is ', root1
            else:
                print '\nThe solutions are: ', root1, root2
        except ValueError as excObj:
            if str(excObj) == 'math domain error':
                print 'Error! No real roots'
            else:
                print 'You did\'t give me the right number of coefficients.'
        except NameError:
            pass
        except TypeError:
            pass
        except SyntaxError:
            pass
        except:
            pass


    main()

if __name__ == ' ':

    def main():
        try:
            num1, num2 = eval(raw_input('Enter two numbers, separated by a comma: '))
            result = num1 / num2
        except ZeroDivisionError:
            print 'Division by zero!'
        except SyntaxError:
            print 'A comma may be missing the input!'
        except:
            print 'Something wrong in the input!'
        else:
            print 'No exceptions, the result is', result
        finally:
            print 'Executing the final caluse'

    main()


if __name__ == '__main__':
    def main1():
        numbers = eval(raw_input('Enter some numbers, separated of comma: '))
        max = numbers[0]
        for i in numbers[1:]:
            if i > max:
                max = i
        print 'The largest number is', max


    def main():
        sum = 0.0
        i = 0
        while True:
            n = raw_input('Enter a number: (enter \'q\' to quit)')
            if n == 'q':
                break
            sum += float(n)
            i += 1
            print '\nThe avg is', sum / i
        print 'Thank you'
    main()


    def main2():
        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    print n, 'equals', x, '*', n // x
                    break
            else:
                print n, 'is a prime number.'



















