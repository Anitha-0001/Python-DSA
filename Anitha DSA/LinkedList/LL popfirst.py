def pop_first(self,value):
    if self.length==0:
        return None
    temp=self.head
    self.head=temp.next
    temp.next=None
    self.length-=1
    if self.length==0:
        self.tail=None
    return 