# -*- coding: UTF-8 -*-


""" 线性表: 顺序表 """
class chainTable():
    # 创建线性表
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def DestoryList(self):
        del self.items

    def ClearList(self):
        self.items = []
        return self.items

    def ListLength(self):
        return len(self.items)

    def GetElem(self, element):
        if not self.isEmpty():
            return element in self.items
        else:
            return False

    def LocateElem(self, element):
        if not self.isEmpty():
            # return self.items.index(element) + 1
            for i in range(len(self.items)):
                if self.items[i] == element:
                    return i

            return -1

    def PriorElem(self, element):
        temp = self.LocateElem(element)
        if temp == -1:
            return False
        else:
            if temp == 0:
                return False
            else:
                return self.items[temp-1]

    def NextElem(self, element):
        temp = self.LocateElem(element)
        if temp == -1:
            return False
        else:
            if temp == (len(self.items) - 1):
                return False
            else:
                return self.items[temp+1]

    def ListTraverse(self):
        for i in self.items:
            print i,

    def ListInsert(self, index, element):
        self.items.insert(index, element)

    def ListDelete(self, index):
        del self.items[index]



if __name__ == '__main__':
    m = chainTable()
    m.items = [1, 2, 2, 3, 4, 5, 4, 6, 1]
    # print m.isEmpty()
    # print m.ListLength()
    # print m.ListTraverse()
    # print m.GetElem(1)
    # print m.GetElem(10)
    print m.LocateElem(2)
    print m.LocateElem(6)
    print m.PriorElem(2)
    print m.PriorElem(6)
    print m.PriorElem(1)
    print m.NextElem(2)
    print m.NextElem(1)
    print m.NextElem(6)
    m.ClearList()
    print m.items
    m.DestoryList()
    print m.items














