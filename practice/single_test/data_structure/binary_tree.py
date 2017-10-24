# -*- coding: UTF-8 -*-

# 二叉树
""" 列表实现 """
tree = ['A',
        ['B',
        ['D', [], []],
        ['E', [], []]],
        ['C',
         ['F', [], []],
         []]
        ]
# 实现
def BinaryTree(item):
    return [item, [], []]

def insertLeft(tree, item):
    leftSubtree = tree.pop(1)
    print leftSubtree
    if leftSubtree:
        tree.insert(1, [item, leftSubtree, []])
    else:
        tree.insert(1, [item, [], []])
    return tree

def inserRight(tree, item):
    rightSubtree = tree.pop(2)
    print rightSubtree
    if rightSubtree:
        tree.insert(2, [item, [], rightSubtree])
    else:
        tree.insert(2, [item, [], []])
    return tree

def getLeftChild(tree):
    print tree[1]
    return tree[1]

def getRightChild(tree):
    print tree[2]
    return tree[2]

if __name__ == '__main__':
    tree = BinaryTree('A')
    insertLeft(tree, 'B')
    inserRight(tree, 'C')
    insertLeft(getLeftChild(tree), 'D')
    inserRight(getLeftChild(tree), 'E')
    insertLeft(getRightChild(tree), 'F')
    print tree






















