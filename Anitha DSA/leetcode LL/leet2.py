class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,value):
        self.value=value
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def has_loop(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False   
        
    
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next