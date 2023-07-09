class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
def push(self,value):
    new_node=Node(value)
    if self.height==0:
        self.top=new_node
    else:
        new_node.next=self.top
        self.top=new_node
    self.height+=1