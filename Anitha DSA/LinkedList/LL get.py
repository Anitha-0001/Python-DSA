def get(self,index):
    if index<0 or index>=self.length:
        return None
    temp=self.head
    for i in range(index):
        temp=temp.next
    return temp


