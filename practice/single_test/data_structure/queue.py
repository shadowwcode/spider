# -*- coding: UTF-8 -*-


class Stack():
    """ 模拟栈 """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def stackTraverse(self, arg=True):
        if arg == True:
            for i in self.items:
                print i,
        else:
            for i in self.items[::-1]:
                print i,

    def reset_stack(self):
        self.items = []
        return self.items



# if __name__ == '__main__':
#     s = Stack()
#     print s.isEmpty()
#     print s.items
#     s.push(4)
#     s.push(3)
#     s.push('dog')
#     print s.items
#     print s.peek()
#     print s.size()
#     print s.pop()
#     print s.size()
#     print s.isEmpty()
#     print s.items


# 进制转换
if __name__ == '__main__':

    n = int(raw_input('Input a size(2 or 8 or 16): '))

    my_stack = Stack()

    num = int(raw_input('Input a 10 integer number: '))
    mod = 0

    my_stack.reset_stack()

    if n == 8 or 2:
        while(num != 0):
            mod = num % n
            my_stack.push(mod)
            num = num / n
        # print my_stack.items
        my_stack.stackTraverse(False)
    # elif n == 2:
    #     while(num != 0):
    #         mod = num % 2
    #         my_stack.push(mod)
    #         num /= 2
    #     my_stack.stackTraverse(False)
    elif n == 16:
        while(num != 0):
            mod = num % n
            if mod == 10:
                mod = 'A'
            elif mod == 11:
                mod = 'B'
            elif mod == 12:
                mod = 'C'
            elif mod == 13:
                mod = 'D'
            elif mod == 14:
                mod = 'E'
            elif mod == 15:
                mod = 'F'

            my_stack.push(mod)
            num /= n
        my_stack.stackTraverse(False)
    else:
        print 'Error'





