def pop(self):
    if self.height==0:
        return None
    else:
        temp=self.top
        self.top=self.top.next
        temp.next=None
    self.height-=1 
    return temp