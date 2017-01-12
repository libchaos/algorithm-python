#!/usr/bin/env python
#coding:  utf-8

class Node:

    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next



if __name__ == "__main__":

    n1 = Node(1, None)
    n2 = Node(2, None)
    n1.next = n2
