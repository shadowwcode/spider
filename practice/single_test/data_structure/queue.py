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


if __name__ == '__main__':
    s = Stack()
    print s.isEmpty()
    print s.items
    s.push(4)
    s.push(3)
    s.push('dog')
    print s.items
    print s.peek()
    print s.size()
    print s.pop()
    print s.size()
    print s.isEmpty()
    print s.items

