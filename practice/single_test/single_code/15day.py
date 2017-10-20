# -*- coding: UTF-8 -*-


# 56
if __name__ == ' ':
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310-k, 250-k, 310+k, 250 + k, width=1)
        k += j
        j += 0.3

    # mainloop()


# 57
if __name__ == '  ':
    from Tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()



# 61 杨辉三角形
if __name__ == '__main__':
    def triangles():
        L = [1]
        while True:
            yield L
            L.append(0)
            L = [L[i - 1] + L[i] for i in range(len(L))]

    a = triangles()
    print a
    print a.next()
    print a.next()
    print a.next()
    print a.next()
    print a.next()

if __name__ == ' ':
    def triangels():
        ret = [1]
        while True:
            yield ret
            for i in range(1, len(ret)):
                ret[i] = pre[i] + pre[i - 1]
            ret.append(1)
            pre = ret[:]

    a = triangels()
    print a.next()
    print a.next()
    print a.next()
    print a.next()
    print a.next()


if __name__ == ' ':
    def YangHui(num=10):
        LL = [1]
        for i in range(1, num):
            LL.append([(0 if j == 0 else LL[i - 1][j - 1]) + (0 if j == len(LL[i - 1]) else LL[i - 1][j]) for j in
                       range(i + 1)])
        return LL


    print YangHui()

