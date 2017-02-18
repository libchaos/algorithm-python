#!/usr/bin/env python
#coding: utf-8

class TreeNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def createTree():
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    E.left = G
    F.left = H
    F.right = I

    return A

def preOrder(node):
    if node is None:
        return
    print node.data
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if node is None:
        return
    
    inOrder(node.left)
    print node.data
    inOrder(node.right)
def postOrder(node):
    if node is None:
        return
    
    postOrder(node.left)
    postOrder(node.right)
    print node.data


def preOrderIter(root):
    s = []#记录的是你访问过的根
    node = root

    while True:
        while node:
            print node
            s.append(node)
            node = node.left
        if not s:
            break
        node = s.pop().right


from collections import deque

def levelOrder(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        

def depth(node):
    if node is None:
        return 0
    dl = depth(node.left)
    dr = depth(node.right)

    return max(dl, dr) + 1


def depth2(root):
    q = deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if node.left:
            q.append((node.left, d+1))
        if node.right:
            q.append((node.right, d+1))
    return d


def copyTree(node):
    if node is None:
        return None
    lt = copyTree(node.left)
    rt = copyTree(node.right)
    return TreeNode(node.data, lt, rt)


def count(n):
    # root : 1
    # left: K [0, n-1]
    # right : n - k - 1
    # if n == 0:
    #     return 1
    s = count.cache.get(n, 0)
    if s:
        return s

    for k in xrange(n):
        s += count(k) *  count(n - 1 - k)
    count.cache[n] = s
    return s
count.cache = {0: 1}


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
    def search(self, k):
        node, _ = self._search(k)
       
        return node
    
    def _search(self, k):

        parent = None
        node = self.root
        while node and node.data != k:
            parent = node
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return node, parent
    
    def insert(self, k):
        node, parent = self._search(k)
        if node:
            return 
        node = TreeNode(k)
        if parent is None:
            self.root = node
        elif k < parent.data:
            parent.left = node
        else:
            parent.right = node
    def delete(self, k):
        pass

if __name__ == "__main__":
    root = createTree()
    newTree = copyTree(root)
   

    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    levelOrder(bst.root)
    print bst.search(5)
