class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first.next=self.first
            temp.next=None
        self.length-=1
        return temp
    
    