class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
def enqueue(self,value):
    new_node=Node(value)
    if self.length==0:
        self.first=new_node
        self.last=new_node
    else:
         self.last.next=new_node
         self.last=new_node
    self.length+=1
    