def pop_first(self):
    if self.length==0:
        return None
    else:
        temp=self.head
        self.head=temp.next
        self.head.prev=None
        temp.next=None
    self.length-=1
    return temp