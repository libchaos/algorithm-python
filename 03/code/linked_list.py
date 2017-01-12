#!/usr/bin/env python
#coding: utf-8

from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def prepend(self, elem):
        self.head = Node(elem)
    def pop(self):
        """
         Get the HEAD Node   
        """
        if self.head is None:
            raise ValueError
        
        e = self.head.elem
        self.head = self.head.next
        return e

    def append(self, elem):
        if self.head is None:
            self.head = Node(elem, None)
            return 
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(elem, None)
    
    def poplast(self):
        if self.head is None:
            raise ValueError
        p = self.head
        if p.next is None:
            e = p.elem
            self.head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e
    
    def find(self, pred):
        p = self.head
        while p is None:
            if pred(p.elem):
                return p.elem
            p = p.next
        return None
    
    def printAll(self):
        p = self.head
        while p is not None:
            print p.elem

            p = p.next

    
