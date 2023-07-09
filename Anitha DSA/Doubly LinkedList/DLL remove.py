def remove(self,index):
    if index<0 or index>=self.length:
        return None
    if index==0:
        return self.pop_first()
    if index==self.length-1:
        return self.pop()
      
    before=self.get(index-1) #temp=self.get(index)
    after=before.next.next   #temp.prev.next=temp.next
                             #temp.next.prev=temp.prev
    before.next=after        #temp.next=None
    after.prev=before        #temp.prev=None
    self.length+=1           
    return True              #return temp