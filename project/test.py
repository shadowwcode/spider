# -*- coding: UTF-8 -*-


import turtle
import time

def drawSnak(rad, angle, len, neckrad):
    colors = ['red', 'yellow', 'purple', 'blue', 'green']
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
        turtle.color(colors[i])
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnak(40, 80, 5, pythonsize/2)
    time.sleep(3)

main()

# turtle.seth(0)
# turtle.fd(200)
# turtle.seth(120)
# turtle.fd(200)
# turtle.seth(240)
# turtle.fd(200)
# 优化
# for i in range(3):
#     turtle.fd(200)
#     turtle.seth((i+1) * 120)
# turtle.done()

# turtle.speed("fastest")
# turtle.pensize(2)
# for i in range(200):
#     turtle.fd(2*i)
#     turtle.left(90)
# time.sleep(3)

# turtle.pensize(2)
# turtle.bgcolor('black')
# colors = ['red', 'yellow', 'purple', 'blue']
# turtle.speed('fastest')
# # turtle.tracer(False)
# for x in range(400):
#     turtle.fd(2 * x)
#     turtle.color(colors[x % 4])
#     turtle.left(91)
# # turtle.tracer(True)
# turtle.done()




if __name__ == ' ':

    val = raw_input('Please input a number(eg: 32C): ')

    if val[-1] in ['C', 'c']:
        f = 1.8 * eval(val[:-1]) + 32
        print('%.2fF' % f)
    elif val[-1] in ['F', 'f']:
        c = (eval(val[:-1]) - 32) / 1.8
        print('%.2fC' % c)




















