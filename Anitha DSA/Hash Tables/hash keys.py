class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size 
        
    def hash(self,key):
        my_hash=0
        for i in key:
            my_hash=(my_hash+ord(i)*23)%len(self.data_map)
        return my_hash
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":",val)
    def set_hash(self,key,value):
        index=self.hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])
                
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys       
     
my_hash_table =HashTable()
my_hash_table.set_hash("a",1)
my_hash_table.set_hash("v",2)
my_hash_table.print_table()
print(my_hash_table.keys())