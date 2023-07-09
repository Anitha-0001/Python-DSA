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
    
    def __r_insert(self,current_node,value):
        if current_node==None:
            return Node(value)
        if value < current_node.value:
            current_node.left=self.__r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right=self.__r_insert(current_node.right,value)
        return current_node     
        
    def r_insert(self,value):
        if self.root==None:
            self.root=Node(value)
        self.__r_insert(self.root,value)
                
my_tree=rBinarySearchTree()
my_tree.r_insert(6)
my_tree.r_insert(7)
my_tree.r_insert(5)

print("root:",my_tree.root.value)
print("root right:", my_tree.root.right.value)
print("root left:", my_tree.root.left.value)