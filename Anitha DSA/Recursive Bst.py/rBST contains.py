class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class rBinarySearchTree:
    def __init__(self):
        self.root=None
    def __r_contains(self,current_node,value):
        if current_node==None:
            return False
        if value==current_node.value:
            return True
        if value<current_node.value:
            return self.__r_contains(current_node.left,value)
        if value> current_node:
            return self.__r_contains(current_node.right,value)
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def insert(self,value):
        new_node= Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
                
my_tree=rBinarySearchTree()
my_tree.insert(6)
my_tree.insert(7)
my_tree.insert(5)

print(my_tree.r_contains(5))
print(my_tree.r_contains(4))
