# -*- coding: UTF-8 -*-
""" 链表 """

# 单链表

class Node:
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        """ 用来定义Node的字符输出, print 为输出 data """
        return str(self.data)


class ChainTable:

    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    # 增加链表(在链表末尾加)
    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    # 删除一个节点
    def delete(self, index):
        if self.isEmpty():
            print "This chain table is empty"
            return

        if index < 0 or index >= self.length:
            print "Error: Out of index!"
            return

        # 删除第一个节点的情况
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev 为保存前导节点
        # node 为保存当前节点
        # 当j和index相等时就相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j > index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1



    # 修改一个节点
    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print 'Error: out of index!'
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    # 查找
    














