#!/usr/bin/env python


class SeqList:

    def __init__(self, dataList=None):
        self.dataList= []
    
    def is_empty(self):
        return True if len(this.dataList) == 0  else False
    
    def length(self):
        return len(self.dataList)
    
    def preappend(self, data):
        self.dataList.insert(0, data)

    def insert(self, elem, i):
        if i < 0 or i >= len(self.dataList):
            raise IndexError
        
        self.dataList.insert(i, elem)
    
    def del_last(self):
        self.dataList.pop()
    def del_first(self):
        self.dataList.remve(self.dataList[0])
    
    def forall(self, fn):
        new_data_list = []
        for i in self.dataList:
            new_data_list.append(fn(i))
        
            
