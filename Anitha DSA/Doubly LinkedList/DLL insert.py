class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    
def insert(self,index,value):
    if index<0 or index>=self.length:
        return None
    if index==0:
        return self.prepend(value)
    if index== self.length:
        return self.append(value)
    
    new_node=Node(value)
    before= self.get(index-1)
    after=before.next
    
    new_node.prev=before
    new_node.next=after
    before.next=new_node
    after.prev=new_node
    self.length+=1
    return True